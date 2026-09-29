# Part 1 of en live.json modules
PART1 = {
  "signals": {
    "aria": {
      "confused": "Signal that concept is unclear",
      "slower": "Request slower pace from instructor"
    },
    "confused": "I didn't understand",
    "sent": "Recorded",
    "slower": "Go slower"
  },
  "reactions": {
    "throttled": "Slow down a bit — your reactions are temporarily limited."
  },
  "pulse": {
    "confused": "{count, plural, one {# person is confused} other {# people are confused}}",
    "slower": "{count, plural, one {# person wants a slower pace} other {# people want a slower pace}}",
    "title": "Class Pulse",
    "window": "In the last minute"
  },
  "hands": {
    "count": "{count, plural, one {# hand raised} other {# hands raised}}",
    "lower": "Lower hand",
    "lowerAll": "Lower all hands",
    "ordinal": "{count, number}",
    "overflow": "{count, plural, one {# other person is waiting} other {# other people are waiting}}",
    "position": "{count, plural, one {Your turn: #} other {Your turn: #}}",
    "title": "Speaking Queue"
  },
  "notes": {
    "ariaLabel": "Shared class notes",
    "charCount": "{count, number} characters",
    "empty": "Nothing has been written yet",
    "exportLabel": "Text export",
    "exportTitle": "Save as text file (.txt)",
    "placeholder": "Write here… What you write is visible to all participants in real time.",
    "synced": "Synced",
    "syncing": "Edits are synced in real time",
    "title": "Shared Notes"
  },
  "sessionAnalysis": {
    "title": "Session Analysis",
    "loading": "Analyzing…",
    "failed": "Session analysis could not be completed",
    "reviewRequired": "This output is a draft and requires instructor review.",
    "confidence": "Estimated confidence: {value, number, ::percent}",
    "unavailable": "Live session analysis is not available. No summary or educational questions were generated.",
    "truncated": "This analysis covers only part of the stored transcript; session text exceeds the processing limit.",
    "quiz": "Suggested Questions ({count, number})",
    "suggestedAnswer": "Suggested answer: {answer}",
    "sources": "Reference Transcript Excerpts ({count, number})"
  },
  "chat": {
    "anonymousAuthor": "User",
    "channels": {
      "class": "Class",
      "staff": "Staff",
      "table": "Table"
    },
    "empty": "No messages sent yet.",
    "note": {
      "class": "Messages are shared live with all participants via the class channel.",
      "locked": "Chat has been locked by the host. Only the host can send messages.",
      "staff": "This channel is only visible to the instructor and teaching assistants; students cannot see it.",
      "table": "This conversation is only visible to tablemates and instructors."
    },
    "placeholder": "Type a message…",
    "placeholderLocked": "Chat is locked…",
    "rejected": {
      "channel": "This channel is not open to you — your message was not sent.",
      "locked": "Chat is locked — your message was not sent."
    },
    "send": "Send message",
    "tableTarget": "Send to table",
    "unread": "{count, plural, one {#} other {#}}"
  },
  "assistant": {
    "chip": {
      "example": "Give an example",
      "practice": "Create practice question",
      "quiz": "Design a short quiz with answers",
      "summarize": "Summarize this topic"
    },
    "error": {
      "createSession": "Failed to create assistant conversation."
    },
    "hostMode": "Instructor Mode — Questions and exercise design",
    "inputLabel": "Ask Smart Assistant",
    "intro": "Ask about the class topic — answers come from course materials (RAG).",
    "introHost": " As an instructor, you can also generate exercises and quizzes.",
    "label": "Smart Assistant",
    "noAnswer": "No response received. Please ask again.",
    "placeholder": "Type your question…",
    "questionCount": "{count, number} questions",
    "send": "Send question",
    "sendShort": "Send",
    "sessionTitle": "Live Class — {name}",
    "source": "Source",
    "sources": "Sources ({count, number})",
    "title": "Class Smart Assistant",
    "typing": "Writing response…"
  },
  "review": {
    "title": "Academic Review Case",
    "separateDecision": "Receiving a report does not confirm that the class was not held. The decision rests with the faculty academic officer.",
    "pendingDecision": "Absence evidence has been recorded and the case is pending decision.",
    "reportReceived": "Report received",
    "reviewerMissing": "No faculty academic officer assigned; case remains open.",
    "reason": "Description and reason (at least 10 characters)",
    "fileReport": "Submit report",
    "confirmNotHeld": "Confirm not held",
    "rejectNotHeld": "Reject not-held report",
    "requestMakeup": "Request make-up session",
    "start": "Proposed start",
    "end": "Proposed end",
    "submitMakeup": "Submit make-up request",
    "makeupRequested": "Requested make-up time",
    "approveMakeup": "Approve make-up time",
    "rejectMakeup": "Reject make-up request",
    "makeupScheduled": "Make-up session has been scheduled; holding it is not yet confirmed.",
    "notHeld": {
      "confirmed": "Confirmed not held",
      "rejected": "Not-held report rejected"
    },
    "makeup": {
      "approved": "Make-up request approved",
      "rejected": "Make-up request rejected"
    },
    "actionFailed": "Could not perform this action; please try again."
  },
  "breakout": {
    "anonymous": "User",
    "decrease": "Decrease rooms",
    "duration": "Duration: {count, number} minutes",
    "durationLabel": "Duration (minutes)",
    "empty": "Empty",
    "end": "End",
    "increase": "Add room",
    "manualLabel": "Manual assignment",
    "maxRooms": "Maximum {count, number} rooms",
    "memberCount": "{count, number} people",
    "mode": {
      "auto": "Automatic",
      "manual": "Manual",
      "random": "Random"
    },
    "modeLabel": "Assignment method",
    "moved": "You have been moved to this room",
    "noParticipants": "No participants in class yet. You can assign them once others join.",
    "noneOpen": "No active breakout rooms. When rooms are opened by the host, your room will appear here.",
    "open": "Open rooms",
    "phaseNote": "At this stage, participant assignment and per-room chat/notes are active. Separate per-room audio and video require media infrastructure (SFU, Stage 3) and are currently outside this section.",
    "preview": "{people, number} participants will be distributed across {rooms, number} rooms (approx. {per, number} people per room).",
    "roomCountLabel": "Number of rooms",
    "roomFor": "Room for {name}",
    "roomName": "Room {index, number}",
    "title": "Breakout Rooms",
    "unassigned": "You have not been assigned to a room yet. Please wait for the host.",
    "you": "You"
  },
  "panel": {
    "close": "Close",
    "host": {
      "actionsFor": "Host actions for {name}",
      "kick": "Remove",
      "lockChat": "Lock chat",
      "lowerHand": "Lower hand",
      "makePresenter": "Make presenter",
      "mute": "Mute",
      "muteAll": "Mute all",
      "unlockChat": "Unlock chat"
    },
    "people": {
      "note": "Participant list updates in real time. Video feeds will appear once the live media engine connects."
    },
    "tabCount": " ({count, number})",
    "tabs": {
      "analytics": "Analytics",
      "assistant": "Assistant",
      "breakout": "Breakout",
      "chat": "Chat",
      "notes": "Notes",
      "people": "Participants",
      "polls": "Polls",
      "tables": "Tables"
    },
    "transcript": {
      "captionTag": " (Speech)",
      "download": "Download full transcript ⬇",
      "fileHeader": "Class Transcript",
      "fileSuffix": "-transcript.txt",
      "preparing": "Preparing…",
      "privateTag": " (Private)",
      "regionLabel": "Live speech transcript"
    }
  },
  "wb": {
    "canvasLabel": "Shared whiteboard canvas",
    "clearAll": "Clear all",
    "clearAllTitle": "Clear all (Host)",
    "clearConfirm": "Confirm clear all",
    "clearConfirmShort": "Confirm?",
    "clearConfirmTitle": "Click again to confirm",
    "colorGroup": "Color",
    "colorSwatch": "Color {color}",
    "exportPng": "Export PNG",
    "exportPngTitle": "Save as PNG image",
    "hintEmpty": "Whiteboard is empty. Select a tool and draw on the canvas.",
    "hintText": "Type text and press Enter to place it on the board.",
    "itemCount": "{count, plural, one {# item on whiteboard} other {# items on whiteboard}}",
    "lock": "Lock whiteboard",
    "lockTitle": "Lock whiteboard for others",
    "lockedNotice": "Whiteboard has been locked by the host; view only at this time.",
    "lockedTitle": "Whiteboard is locked — click to unlock",
    "redo": "Redo",
    "textLabel": "Text on whiteboard",
    "textPlaceholder": "Text… (Enter to place, Esc to cancel)",
    "toolbarLabel": "Whiteboard tools",
    "tools": {
      "arrow": "Arrow",
      "circle": "Circle",
      "eraser": "Eraser",
      "line": "Line",
      "pen": "Pen",
      "rect": "Rectangle",
      "select": "Select",
      "text": "Text"
    },
    "undo": "Undo",
    "undoTitle": "Undo (your last item)",
    "unlock": "Unlock whiteboard",
    "widthGroup": "Stroke width",
    "widthOption": "Width {width, number}"
  },
  "poll": {
    "addOption": "Add option",
    "cancel": "Cancel",
    "changeHint": "To change your vote, select another option.",
    "emptyGuest": "There are currently no active polls. When the host starts a poll, it will appear here.",
    "emptyHost": "No active polls. Click \"New Poll\" to create one.",
    "end": "End poll",
    "endedBadge": "Ended",
    "finalTotal": "Final results · Total {count, plural, one {# vote} other {# votes}}",
    "minOptions": "At least {min, number} non-empty options are required to start.",
    "multi": "Multiple choice",
    "multiLabel": "Allow selecting multiple options (Multiple choice)",
    "new": "New poll",
    "optionN": "Option {n, number}",
    "optionTally": "{pct, number}% · {count, number}",
    "optionsLabel": "Options ({used, number} of {max, number})",
    "questionAria": "Question text",
    "questionLabel": "Question",
    "questionPlaceholder": "e.g., Which topic do you prefer?",
    "removeOption": "Remove option",
    "single": "Single choice",
    "start": "Start poll",
    "status": {
      "ended": "Poll has ended — final results.",
      "endingWait": "Waiting for poll end confirmation…",
      "startFailed": "Server did not confirm poll start. Check connection and host permissions and try again.",
      "started": "Poll started — awaiting responses…",
      "starting": "Starting poll…",
      "voteFailed": "Vote submission was not confirmed; please try again.",
      "voteSent": "Your vote was submitted ✓",
      "voting": "Submitting vote…",
      "waitingAnswers": "Awaiting responses…"
    },
    "submitVote": "Submit vote",
    "title": "Poll",
    "updateVote": "Update vote",
    "voteCount": "{count, plural, one {# vote} other {# votes}}"
  },
  "preflight": {
    "bandwidth": {
      "detail": "Your internet connection was detected as weak; camera video will be sent at lower quality to avoid interruptions.",
      "good": "Good",
      "label": "Internet connection quality",
      "unknown": "Unknown",
      "weak": "Weak"
    },
    "captions": {
      "available": "Available",
      "detail": "Browser speech-recognition based live captions and translation only work in Chrome/Edge. Other class features remain fully accessible without it.",
      "label": "Live captions (optional)",
      "limited": "Limited"
    },
    "device": {
      "absentDetail": "No active {device} found. Check device connection; you can still enter the class without {device}.",
      "absentStatus": "Not found",
      "camera": "Camera",
      "deniedDetail": "Access to {device} was denied. Click the lock icon next to the address bar and set \"{device}\" to Allow. You can still enter without it.",
      "deniedStatus": "Access denied",
      "microphone": "Microphone",
      "promptDetail": "Permission to access {device} has not been granted yet. Select Allow when prompted by your browser.",
      "promptStatus": "Awaiting permission",
      "readyStatus": "Ready"
    },
    "panel": {
      "blocked": "You cannot enter the class until the red item(s) above are resolved. Once fixed, click \"Re-check\".",
      "checking": "Checking…",
      "regionLabel": "Device readiness check before entry",
      "retry": "Re-check",
      "severity": {
        "fail": "Issue",
        "pass": "Ready",
        "warn": "Warning"
      },
      "title": "Device Readiness Check"
    },
    "screen": {
      "detail": "Your browser does not support screen sharing. If you plan to present, use Chrome/Edge or desktop Firefox. It is not required for viewing the class.",
      "label": "Screen sharing"
    },
    "secure": {
      "bad": "Insecure",
      "detail": "This page is not opened over a secure connection (HTTPS); browsers only grant camera and microphone access on HTTPS. Please open the URL with https.",
      "label": "Secure connection (HTTPS)",
      "ok": "Secure"
    },
    "supported": "Supported",
    "unsupported": "Not supported",
    "webrtc": {
      "detail": "Your browser does not support camera/microphone access (getUserMedia). Please use an up-to-date version of Chrome, Edge, or desktop Firefox.",
      "label": "Video call support (WebRTC)"
    }
  },
  "guide": {
    "button": "Guide",
    "lobby": {
      "chain": {
        "check": "Here you test your name, camera, and microphone and complete the readiness checklist.",
        "enter": "At class time, enter this pre-room from there.",
        "join": "Upon entering the class, you are transferred to the live room; the guide continues there."
      },
      "ifEmpty": "If the class has not started yet, wait for the host; connection status updates on this same page.",
      "intro": "Welcome to the pre-room for the live class. Here you check your sound, picture, and connection before entering.",
      "roles": {
        "host": {
          "does": "Enters the room, welcomes students, and starts the class.",
          "label": "Host (Instructor)"
        },
        "student": {
          "does": "Tests camera/microphone, checks readiness, and enters the class.",
          "label": "You (Student)"
        }
      },
      "title": "Pre-room Guide",
      "youCan": {
        "cam": "Turn your camera on/off with the camera button.",
        "enter": "When ready, click \"Enter Class\".",
        "mic": "Turn your microphone on/off with the microphone button.",
        "settings": "Change camera, microphone, or speaker device from the settings column."
      }
    },
    "roles": "Who does what",
    "youCan": "What can you do here?",
    "session": {
      "chain": {
        "participate": "During class you participate via microphone/camera/chat; the host controls the class flow.",
        "record": "If the host enables recording, the recording becomes available after class ends.",
        "review": "You return from \"Recordings\" to review a missed class or study.",
        "start": "The host (instructor) starts the live class; you join the room."
      },
      "ifEmpty": "If class hasn't started yet, wait for the host; connection status updates on this page.",
      "intro": "This page is your live class room with microphone/camera, screen sharing, chat, and Q&A. The host (instructor) manages the class and records if needed.",
      "roles": {
        "host": {
          "does": "Starts/controls the class and enables recording if needed.",
          "label": "Host (Instructor)"
        },
        "student": {
          "does": "Joins the class, participates, and watches recordings later if needed.",
          "label": "You (Student)"
        }
      },
      "title": "Live Class Guide",
      "youCan": {
        "chat": "Send messages or ask questions in writing using \"Chat\".",
        "media": "Turn your microphone and camera on/off from the bottom bar.",
        "recordings": "After class ends, watch the recording under \"Recordings\" if recorded.",
        "share": "Share your screen if permitted by the host."
      }
    }
  },
  "analytics": {
    "anonymous": "User",
    "attendance": {
      "absentChip": "✗ Absent {count, number}",
      "absentLabel": "Absent",
      "avatarFallback": "?",
      "duration": "Duration: {value}",
      "empty": "No attendance recorded yet. As participants join, they will appear here.",
      "excusedChip": "Excused {count, number}",
      "excusedLabel": "Excused",
      "finalized": "Finalized",
      "inClass": "In class",
      "joinedAt": "Joined: {time}",
      "lateChip": "⏰ Late {count, number}",
      "lateLabel": "Late",
      "left": "Left",
      "loading": "Loading attendance…",
      "neverOpened": "This session was not held (no attendance recorded).",
      "presentChip": "✓ Present {count, number}",
      "presentLabel": "Present",
      "provisional": "Provisional (until class ends)",
      "refreshNote": "{count, number} people · Updates every {seconds, number} seconds",
      "stillPresent": " (Currently attending)",
      "title": "Attendance List"
    },
    "duration": {
      "hours": "{count, number} hours",
      "hoursMinutes": "{hours, number} hours and {minutes, number} minutes",
      "lessThanMinute": "Less than 1 minute",
      "minutes": "{count, number} minutes"
    },
    "error": {
      "attendance": "Could not retrieve attendance list. This section is only available to the host."
    },
    "participation": {
      "aria": "Microphone open {on, number} of {total, number}",
      "empty": "No one is in the class yet.",
      "muted": "Muted: {count, number}",
      "on": "Open: {count, number} ({pct, number}%)",
      "title": "Audio Participation"
    },
    "poll": {
      "active": "A poll is currently active",
      "idle": "No active polls"
    },
    "stat": {
      "chat": "Chat messages",
      "hands": "Hands raised",
      "micOn": "Open mics",
      "present": "Currently present"
    }
  },
  "lobby": {
    "back": "Back to workspace",
    "removedByHost": "You have been removed from this class. Rejoining is only possible after instructor permission.",
    "removedServiceDesk": "Submit ticket at Service Desk",
    "cam": {
      "off": "Turn camera off",
      "on": "Turn camera on",
      "stateOff": "Camera off",
      "stateOn": "Camera on"
    },
    "camOffOverlay": "Camera is off",
    "conn": {
      "fair": "Fair",
      "good": "Good",
      "poor": "Poor",
      "title": "Connection Quality",
      "unknown": "Unknown"
    },
    "cta": {
      "blocked": "To enter the class, the critical prerequisites above (secure connection and browser support) must be resolved.",
      "blockedTitle": "Cannot enter until critical prerequisites are resolved",
      "enter": "Enter Class",
      "ready": "Check your video and audio before entering.",
      "waiting": "The instructor has not entered yet; you may enter and wait."
    },
    "device": {
      "camera": "Camera",
      "cameraNone": "No camera found",
      "fallback": "{device} {index, number}",
      "mic": "Microphone",
      "micNone": "No microphone found",
      "speaker": "Speaker",
      "speakerDefault": "System default speaker"
    },
    "fallbackTitle": "Live Class",
    "guest": "Guest",
    "help": {
      "body": "Before entering the live class, test your camera, microphone, and speaker here. Use the buttons below the preview to toggle camera or microphone and change devices in the settings column. When everything is ready, click \"Enter Class\".",
      "title": "Class Entry Guide"
    },
    "joinMuted": "Enter with microphone muted",
    "loading": "Loading session details…",
    "media": {
      "denied": "Camera or microphone access was not granted.",
      "deniedTitle": "Camera/microphone access denied",
      "notFound": "Camera or microphone device not found."
    },
    "meta": {
      "host": "Instructor: {name}",
      "time": "Time: {time}"
    },
    "meter": {
      "label": "Microphone level",
      "micOff": "Microphone is muted — unmute to test."
    },
    "mic": {
      "off": "Mute microphone",
      "on": "Unmute microphone",
      "stateOff": "Microphone muted",
      "stateOn": "Microphone active"
    },
    "perm": {
      "retry": "Retry permission request",
      "step1": "Click the lock icon next to the browser address bar.",
      "step2": "Set \"Camera\" and \"Microphone\" permissions to \"Allow\".",
      "step3": "Then click the button below to retry.",
      "without": "You can also enter the class without camera/microphone."
    },
    "settings": {
      "name": "Your display name in class",
      "title": "Audio & Video Settings"
    },
    "speaker": {
      "playing": "Playing…",
      "test": "Test"
    },
    "status": {
      "ended": "This session has ended",
      "live": "In progress",
      "prefix": "Status: {status}",
      "waiting": "Instructor has not entered yet"
    }
  }
}
