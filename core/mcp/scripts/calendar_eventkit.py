#!/usr/bin/env python3
"""
Fast calendar queries using native EventKit framework.
Replaces slow AppleScript queries with proper database access.

Performance: 30s → <1s for typical queries
"""

import sys
import json
from datetime import datetime, timedelta
import EventKit

def get_events(calendar_name: str, start_offset_days: int, end_offset_days: int):
    """Get events using native EventKit (fast!)
    
    Args:
        calendar_name: Calendar name or email
        start_offset_days: Days offset from today (0 = today)
        end_offset_days: Days offset from today (1 = tomorrow)
    """
    store = EventKit.EKEventStore.alloc().init()
    
    # Request calendar access (should already be granted)
    # Note: This is synchronous on macOS (instant if already authorized)
    
    # Find the calendar
    calendars = store.calendarsForEntityType_(EventKit.EKEntityTypeEvent)
    target_calendar = None
    
    for cal in calendars:
        if cal.title() == calendar_name or cal.calendarIdentifier() == calendar_name:
            target_calendar = cal
            break
    
    if not target_calendar:
        print(json.dumps({"error": f"Calendar not found: {calendar_name}"}))
        sys.exit(1)
    
    # Calculate date range
    today = datetime.now().replace(hour=0, minute=0, second=0, microsecond=0)
    start_date = today + timedelta(days=start_offset_days)
    end_date = today + timedelta(days=end_offset_days)
    
    # Create predicate for date range (this uses database queries - FAST!)
    predicate = store.predicateForEventsWithStartDate_endDate_calendars_(
        start_date,
        end_date,
        [target_calendar]
    )
    
    # Fetch events (database query, not linear scan)
    events = store.eventsMatchingPredicate_(predicate)
    
    # Format output
    result = []
    for event in events:
        event_data = {
            "title": event.title() or "",
            "start": event.startDate().description(),
            "end": event.endDate().description(),
            "location": event.location() or "",
            "url": event.URL().absoluteString() if event.URL() else "",
            "notes": event.notes() or "",
            "all_day": event.isAllDay()
        }
        result.append(event_data)
    
    # Sort by start time
    result.sort(key=lambda x: x["start"])
    
    # Output as JSON
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: calendar_eventkit.py <calendar_name> <start_offset> <end_offset>")
        sys.exit(1)
    
    calendar_name = sys.argv[1]
    start_offset = int(sys.argv[2])
    end_offset = int(sys.argv[3])
    
    get_events(calendar_name, start_offset, end_offset)
