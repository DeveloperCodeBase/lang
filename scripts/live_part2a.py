# Part 2A of en live.json: tables, classes, atoms
PART2A = {
  "tables": {
    "assign": {
      "balanced": "Automatic (balanced)",
      "noStudents": "No students in class yet.",
      "pickFor": "Table for {name}",
      "random": "Random",
      "title": "Seat students",
      "unassigned": "Unassigned"
    },
    "cancel": "Cancel",
    "confirm": "Yes",
    "countLabel": "Number of new tables",
    "capacity": "{used, number} of {total, number} people",
    "capacityLabel": "Capacity per table",
    "create": "Create table",
    "defaultName": "Table {index, number}",
    "dissolve": "Dissolve table",
    "dissolveConfirm": "Dissolve \"{name}\"? Its members will return to the main class.",
    "duration": {
      "label": "Table work duration",
      "option": "{count, number} minutes"
    },
    "empty": "No tables created yet.",
    "extend": "{count, number} more minutes",
    "limit": "Maximum {count, number} tables",
    "mediaNote": "During table work, only your tablemates see and hear you.",
    "memberCount": "{count, number} people",
    "members": "Tablemates",
    "nameLabel": "Table name",
    "peekNotice": "Instructor is monitoring tables",
    "rejected": {
      "empty": "No tables have members.",
      "full": "This table is full.",
      "error": "An error occurred; please try again.",
      "forbidden": "You do not have permission for this action.",
      "invalid": "Invalid request.",
      "limit": "You have reached the maximum number of tables.",
      "noRound": "Table work has not started.",
      "notFound": "This table no longer exists.",
      "roundActive": "This action cannot be performed while table work is in progress.",
      "selectionLocked": "Table selection is locked by the instructor."
    },
    "remaining": "Time remaining: {time}",
    "rename": "Rename",
    "returnAll": "Return all",
    "returnAllConfirm": "Return everyone to the main class?",
    "returned": "Everyone returned to the main class.",
    "running": "Table work in progress",
    "save": "Save",
    "select": {
      "action": "Select table",
      "full": "Full",
      "hint": "Select an open table; you can change it as long as the instructor leaves selection open.",
      "selected": "Your table",
      "title": "Select Table"
    },
    "selection": {
      "close": "Close student selection",
      "open": "Open student selection"
    },
    "start": "Start table work",
    "startHint": "At least one table with members is required.",
    "timeUp": "Table time has ended; everyone returned to the main class.",
    "title": "Group Tables",
    "transcriptConsentProgress": "Voice transcript consent: {accepted} of {total}",
    "transcriptDurableEnabled": "Persistent recording is active only with everyone's consent.",
    "transcriptConsentAccept": "Consent to table audio recording",
    "transcriptConsentWithdraw": "Withdraw consent",
    "transcriptWithdrawalReason": "Reason for withdrawing consent",
    "transcriptQuarantined": "This table's transcript is quarantined for safe recreation.",
    "transcriptConsentUnavailable": "Table transcript consent status is unavailable.",
    "visit": {
      "join": "Join",
      "joined": "You are at \"{name}\"",
      "leave": "Return to main class",
      "peek": "Listen quietly",
      "peeking": "Listening to \"{name}\""
    },
    "you": {
      "assigned": "You are at \"{name}\"",
      "unassigned": "You have not been assigned to a table yet.",
      "waiting": "Table work has not started yet."
    }
  },
  "classes": {
    "card": {
      "attendees": "{value, number} participants",
      "cancelled": "This session has been cancelled.",
      "joinDirect": "Direct Entry",
      "joinLobby": "Enter Lobby",
      "newTab": "Open in new tab",
      "report": "Session Report",
      "reportTitle": "Complete report for this session"
    },
    "emptyAll": "No sessions match your search.",
    "emptyUpcoming": "No upcoming sessions.",
    "filter": {
      "all": "All",
      "cancelled": "Cancelled",
      "ended": "Ended",
      "live": "Live Now",
      "scheduled": "Scheduled"
    },
    "filterAria": "Filter live sessions",
    "guide": {
      "body": "All your live classes, upcoming sessions, and past sessions are listed here. Click \"Enter Lobby\" to test your camera and microphone before entering class; if a session is currently live, click \"Direct Entry\" to join immediately. Instructors and administrators can schedule a new live class with \"New Session\".",
      "title": "Live Classes Guide"
    },
    "kpi": {
      "live": "Live Now",
      "total": "Total Sessions",
      "upcoming": "Upcoming"
    },
    "lead": "View live, upcoming, and past sessions here; enter the lobby to test your camera and microphone or — if a session is live — join the class directly.",
    "loading": "Loading sessions…",
    "new": "New Session",
    "noCourse": "No associated course",
    "policy": {
      "enrolled": "Enrolled students only",
      "invite": "Invitation only",
      "public": "Open to all (Public)"
    },
    "schedule": {
      "at": "{date} · {clock}",
      "unknown": "Time unspecified"
    },
    "searchAria": "Search sessions",
    "searchPlaceholder": "Search by title, course, or instructor…",
    "status": {
      "cancelled": "Cancelled",
      "ended": "Ended",
      "live": "Live Now",
      "scheduled": "Scheduled"
    },
    "title": "Live Classes"
  },
  "atoms": {
    "captions": {
      "etaTradeoff": "If η is too large, the cost function diverges; if too small, convergence is slow.",
      "fasterNoisier": "This causes updates to be faster but more oscillating.",
      "lrAnswer": "Good question. We typically combine it with a Learning Rate Scheduler or Adam.",
      "lrQuestion": "Professor, how is the optimal learning rate selected for SGD?",
      "sgdStep": "Stochastic Gradient Descent uses only one sample per step to compute the gradient."
    },
    "chat": {
      "seed": {
        "answer": "Sure. Suppose θ = 0.8, gradient = 2.4, and η = 0.1. Then:",
        "answerTime": "14:25",
        "ask": "Can you provide a numerical example of weight updates in SGD?",
        "askTime": "14:25",
        "greeting": "Hello 👋 I am the smart assistant for this session. I can provide real-time summaries, simplify concepts, or suggest extra practice exercises.",
        "greetingTime": "14:23"
      }
    },
    "people": {
      "ali": {
        "init": "A",
        "name": "Ali R."
      },
      "arman": {
        "init": "A",
        "name": "Arman B."
      },
      "azimi": {
        "init": "DA",
        "name": "Dr. Azimi"
      },
      "hanieh": {
        "init": "H",
        "name": "Hanieh F."
      },
      "mohsen": {
        "init": "M",
        "name": "Mohsen H."
      },
      "neda": {
        "init": "N",
        "name": "Neda Kazemi"
      },
      "nima": {
        "init": "N",
        "name": "Nima J."
      },
      "sara": {
        "init": "S",
        "name": "Sara M."
      },
      "zahra": {
        "init": "Z",
        "name": "Zahra K."
      }
    },
    "poll": {
      "options": {
        "adamWeighted": "Adam with class weighting",
        "rmspropWarmup": "RMSprop with Warm-up",
        "sgdMomentum": "Standard SGD with Momentum"
      },
      "question": "Which optimization method is best suited for training deep networks on imbalanced data?"
    },
    "qa": {
      "q1": {
        "text": "If the cost function is non-convex, does SGD converge to a global minimum?",
        "time": "2 minutes ago"
      },
      "q2": {
        "text": "What is the practical difference between Momentum and Adam?",
        "time": "5 minutes ago"
      },
      "q3": {
        "text": "What mini-batch size is recommended for ResNet-50?",
        "time": "8 minutes ago"
      },
      "q4": {
        "text": "What settings should be applied to SGD for imbalanced datasets?",
        "time": "12 minutes ago"
      },
      "tags": {
        "adaptive": "Adaptive",
        "highlight": "Highlight",
        "practical": "Practical"
      }
    },
    "slides": {
      "compare": {
        "body": "Mini-batch strikes a balance between Batch stability and SGD speed. Typical size: 32 to 256."
      },
      "noise": {
        "body": "Random fluctuations allow the algorithm to escape local minima and perform better on non-convex surfaces.",
        "title": "Why noise is useful"
      },
      "sgd": {
        "body": "In each step, weights are updated with a single random data sample. Faster than Batch GD but with more oscillation along the convergence path.",
        "title": "Stochastic Gradient Descent"
      }
    },
    "suggestions": {
      "exercise": "Generate similar exercise",
      "resources": "Additional resources",
      "simpler": "Explain more simply",
      "summary": "Summary of the last 2 minutes"
    },
    "tabs": {
      "assistant": "Assistant",
      "captions": "Captions",
      "poll": "Poll",
      "questions": "Questions"
    },
    "timeline": {
      "r1": {
        "label": "Previous session review",
        "time": "14:02"
      },
      "r2": {
        "label": "Gradient descent concept",
        "time": "14:08"
      },
      "r3": {
        "label": "Batch version",
        "time": "14:16"
      },
      "r4": {
        "label": "Stochastic Gradient Descent",
        "time": "14:22"
      },
      "r5": {
        "label": "Momentum and Adam",
        "time": "14:35"
      },
      "r6": {
        "label": "Interactive exercise + Q&A",
        "time": "14:45"
      }
    },
    "transcript": {
      "live": {
        "momentum": "If we update learning taking into account previous values, that is called Momentum.",
        "nesterovAnswer": "Nesterov first predicts the next position and computes the gradient there.",
        "nesterovQuestion": "How does this differ from Nesterov?",
        "pytorchQuestion": "Can this idea be implemented in PyTorch?"
      },
      "seed": {
        "r1": {
          "text": "In stochastic gradient descent, only one sample is used to compute the gradient at each step.",
          "time": "14:20"
        },
        "r2": {
          "text": "This increases computation speed and decreases memory usage.",
          "time": "14:21"
        },
        "r3": {
          "highlight": "Optimal learning rate",
          "text": "Professor, how is the optimal learning rate chosen?",
          "time": "14:22"
        },
        "r4": {
          "text": "Usually we combine it with a Learning Rate Scheduler or adaptive algorithms like Adam.",
          "time": "14:22"
        },
        "r5": {
          "text": "What is the exact key difference between SGD and Mini-batch?",
          "time": "14:23"
        },
        "r6": {
          "text": "Batch size. In Mini-batch we take between 32 and 256 samples for a better balance between stability and speed.",
          "time": "14:23"
        }
      }
    }
  }
}
