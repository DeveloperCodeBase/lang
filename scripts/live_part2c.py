# Part 2C of en live.json: session
PART2C = {
  "session": {
    "absence": {
      "instructorDisconnected": "Instructor connection lost — class continues until their return.",
      "takeOver": "Accept temporary control of tables and speaking queue"
    },
    "supervision": {
      "waiting": "Class is temporarily without an academic supervisor. Waiting for instructor return or assistant assumption of responsibility.",
      "paused": "Academic supervision was not resumed within the allowed window; recording stopped. Class and content are preserved.",
      "recordingDenied": "To record this class, accepted academic responsibility and valid attendance are required.",
      "offer": "Offer class responsibility to {name}",
      "offerPending": "Responsibility offer sent; until explicit acceptance by assistant, responsibility remains yours.",
      "accept": "Accept academic responsibility for class",
      "conflict": "You are already responsible for another live class. Please end it first or delegate responsibility to an attending and authorized assistant.",
      "returnFirst": "Return to first class",
      "returnLobby": "Return to pre-room"
    },
    "cohost": {
      "denied": "Cannot grant co-host; assistant must be present in this class and assigned to this section.",
      "grant": "Temporarily promote {name}",
      "granted": "You are now temporary co-host of this class.",
      "instructorPresent": "Instructor has returned to class; delegation request not permitted.",
      "manage": "Manage temporary co-host",
      "revoke": "Revoke co-host for {name}",
      "revoked": "Your co-host access has been revoked."
    },
    "kick": {
      "failed": "Student removal was incomplete. Media connection has not closed yet; please try again.",
      "manage": "Students removed from this session",
      "restore": "Allow {name} to rejoin",
      "restoreFailed": "Could not record rejoin permission. Please try again."
    },
    "archive": {
      "btn": "Transcript Archive",
      "download": "Download archive",
      "empty": "No speech stored in archive yet.",
      "error": "Failed to retrieve archive.",
      "loading": "Loading archive…",
      "reload": "Reload",
      "retry": "Try again",
      "short": "Archive",
      "title": "Transcript Archive (Stored)"
    },
    "browserUnknown": "Unknown",
    "capset": {
      "btn": "Caption Settings",
      "fontSize": "Font size",
      "lg": "Large",
      "maxLines": "Maximum display lines",
      "md": "Medium",
      "off": "Off",
      "on": "On",
      "showNames": "Show speaker names",
      "sm": "Small",
      "title": "Caption Display Settings"
    },
    "captions": {
      "cpuSlow": "Speech processing on current server CPU is slower than real-time; captions will activate following server upgrade",
      "deviceUnsupported": "Captions not supported on this browser/device; use Safari on iPhone or a laptop",
      "engineStuck": "Browser speech engine is not responding; please try again",
      "fallbackServer": "Browser speech engine not permitted; switched to server engine (may be slower on this server)",
      "micDenied": "Microphone access not granted",
      "micRequired": "Microphone must be active for captions",
      "needMic": "Unmute microphone to enable captions",
      "noNativeNoServer": "Your browser lacks native captions and server speech service is not active",
      "recordFailed": "Audio recording for captions failed",
      "unavailable": "Captions unavailable"
    },
    "close": "Close",
    "collabLoading": "Loading…",
    "conn": {
      "fair": "Fair",
      "good": "Good",
      "poor": "Poor",
      "unknown": "Unknown"
    },
    "connFoot": "Connection quality: {quality} · {count, number} participants",
    "diag": {
      "bitrate": "Bitrate",
      "close": "Close diagnostics",
      "codecs": "Codecs",
      "connType": "Connection Type",
      "copy": "Copy diagnostics",
      "copyDone": "Copied ✓",
      "cpu": "Estimated CPU load",
      "fps": "Framerate",
      "help": "Technical network and media diagnostics for troubleshooting live streaming issues.",
      "jitter": "Jitter",
      "packetLoss": "Packet loss",
      "ping": "Round-trip time (RTT)",
      "refresh": "Refresh stats",
      "resolution": "Resolution",
      "rtt": "Latency",
      "title": "Technical Connection Diagnostics",
      "turn": "Relay Server (TURN)",
      "webrtc": "WebRTC Engine"
    },
    "download": {
      "chat": "Download chat",
      "csv": "Export CSV",
      "json": "Export JSON",
      "notes": "Download notes",
      "pdf": "Export PDF",
      "title": "Downloads & Exports",
      "txt": "Download TXT"
    },
    "end": {
      "action": "End session",
      "cancel": "Cancel",
      "confirm": "Are you sure you want to end this live session for everyone?",
      "confirmShort": "End class?",
      "desc": "Ending the session will disconnect all attendees and finalize the attendance report.",
      "done": "Session has ended.",
      "failed": "Could not end session; please try again.",
      "title": "End Class Session",
      "wait": "Ending session…"
    },
    "ended": {
      "body": "The host has ended this live class. Thank you for attending.",
      "cta": "Return to Course",
      "title": "Class Ended"
    },
    "film": {
      "aria": "Participant video filmstrip",
      "hide": "Hide filmstrip",
      "show": "Show filmstrip"
    },
    "fs": {
      "enter": "Enter fullscreen",
      "exit": "Exit fullscreen",
      "toggle": "Toggle fullscreen"
    },
    "guest": "Guest",
    "jitsi": {
      "connecting": "Connecting to media stream…",
      "error": "Media streaming error. Please refresh."
    },
    "lang": {
      "faShort": "FA"
    },
    "langMenu": {
      "help": "Language in which you view captions",
      "my": "My language: {label}",
      "notFound": "No language found.",
      "searchLabel": "Search language",
      "searchPlaceholder": "Search language…"
    },
    "layout": {
      "custom": "Custom",
      "focusPresentation": "Presentation focus",
      "focusVideo": "Video focus",
      "smart": "Smart"
    },
    "leave": "Leave class",
    "leaveShort": "Leave",
    "media": {
      "audioOnly": "Camera video was unavailable; continuing in audio-only mode.",
      "denied": "Camera/mic access was denied. Click the lock/camera icon in your address bar, allow access, then click \"Retry\".",
      "errSuffix": " (Error: {name})",
      "generic": "Could not access media devices. You may stay in class with camera and mic off.",
      "inUse": "Camera is in use by another app or tab — please close lobby tabs or background apps.",
      "notFound": "No camera or microphone found. Connect a device and click \"Retry\", or continue muted.",
      "retry": "Retry",
      "unsupported": "Your browser does not support camera/mic access or the page is not loaded via secure connection (HTTPS)."
    },
    "panel": {
      "chatTranslated": "Chat (Translated)",
      "empty": "No speech recorded yet.",
      "regionLabel": "Live translated speech",
      "title": "Live Chat (Translated)"
    },
    "participant": "Participant",
    "rec": {
      "active": "Recording",
      "armed": "Ready to record",
      "cancel": "Cancel",
      "netFailed": "Connection to server failed. Please try again.",
      "paused": "Temporarily paused",
      "retry": "Try again",
      "saveCta": "Save to archive",
      "saveFailed": "Failed to save recording (code {code, number}). Please try again.",
      "saveMeta": "File size: {size} MB · Duration: {clock}",
      "saveTitle": "Save recording to archive?",
      "saved": "Recording saved to archive",
      "durableServer": "This segment is recorded on the server.",
      "durablePending": "Segment is held safely in this browser, awaiting server commit.",
      "durableUnprotected": "Active segment is not yet protected; an unexpected crash may lose unsaved data.",
      "recoveryAvailable": "You have an uncommitted safe recording available for recovery.",
      "recoveryOpen": "Recover recording",
      "startFailed": "Failed to start recording. Please try again.",
      "unsupportedRecorder": "Your browser does not support video recording (MediaRecorder). Please use an up-to-date Chrome/Edge or desktop Firefox.",
      "unsupportedScreen": "Your browser does not support screen recording. Please use an up-to-date Chrome/Edge or desktop Firefox.",
      "uploading": "Uploading… {pct, number}%"
    },
    "reconnecting": "Reconnecting…",
    "selfName": "{name} (You)",
    "share": {
      "failed": "Screen sharing failed. Please try again.",
      "unsupported": "Your browser does not support screen sharing. Please use an up-to-date Chrome/Edge or desktop Firefox."
    },
    "someone": "A participant",
    "soniox": {
      "captionFailed": "Live caption stream disconnected; connection could not be restored after several attempts. Class itself continues normally — you can toggle captions again if desired.",
      "connecting": "Live translation: Connecting…",
      "detectedLabel": "Detected:",
      "detectedTitle": "Speaker's detected language",
      "error": "Live translation: Error — Retrying",
      "exportDate": "Export date: {date}",
      "exportHead": "Live Translated Transcript — Session {id}",
      "group": "Live Translation",
      "langSep": ", ",
      "on": "Live translation: On",
      "receiveOnly": "Caption display mode: View speech of others without microphone",
      "saveFallback": "Server save failed — saved locally instead",
      "stConnecting": "Connecting…",
      "stError": "Error",
      "stMore": " +{value, number}",
      "stOn": "On",
      "stOnTargets": "On · → {langs}",
      "stPaused": "Paused (Muted)",
      "stReceiveOnly": "Display only (No mic)",
      "stReconnecting": "Reconnecting…",
      "stTranscribeOnly": "On · Transcription only",
      "turnOn": "Turn on live translation",
      "unavailable": "Live translation unavailable"
    },
    "stage": {
      "captionFeed": "Live translated captions",
      "modeLabel": "Stage mode",
      "noShare": "No presentation shared",
      "noShareHint": "To present, click \"Share Screen\", or select \"Whiteboard\" for collaborative drawing.",
      "share": "Share screen",
      "whiteboard": "Whiteboard"
    },
    "tile": {
      "handRaised": "Hand raised",
      "pin": "Pin {name}",
      "quality": {
        "connecting": "Reconnecting",
        "fair": "Connection quality: Fair",
        "good": "Connection quality: Good",
        "poor": "Connection quality: Poor",
        "unknown": "Connection quality: Unknown"
      }
    },
    "titleFallback": "Live Class",
    "duplicate": {
      "replaced": "You joined from another device; audio and video on this device have been disconnected.",
      "continued": "Previous device connection closed; you are now connected from this device.",
      "continueHere": "Continue on this device"
    },
    "toast": {
      "captionsOn": "Class captions enabled — each speaker's audio labeled with their name",
      "chatLocked": "Chat locked by host",
      "chatUnlocked": "Chat unlocked",
      "joined": "{name} joined",
      "kicked": "You have been removed from the class by the host.",
      "left": "{name} left",
      "recStarted": "Recording started",
      "recStopped": "Recording stopped"
    },
    "toolbar": {
      "cam": "Camera",
      "captionsGroup": "Captions & Translation",
      "ccOff": "Captions (CC)",
      "ccOn": "Captions ✓ ({lang})",
      "ccStarting": "Captions… ({lang})",
      "endClass": "End Class",
      "endClassShort": "End",
      "handShort": "Hand",
      "langEn": "Language: English",
      "langFa": "Language: Persian",
      "layout": "Layout",
      "mic": "Microphone",
      "more": "More",
      "moreLabel": "More controls",
      "panel": "Chat & People",
      "panelShort": "Chat",
      "raiseHand": "Raise Hand",
      "reactions": "Reactions",
      "sendReaction": "Send reaction {emoji}",
      "share": "Share screen",
      "shareShort": "Share"
    },
    "topbar": {
      "elapsedLabel": "Class duration",
      "hostPrefix": "Host: {name}",
      "loadingTitle": "Loading…",
      "recOffTitle": "Recording occurs in the host's browser and is saved to archive upon completion",
      "recOnTitle": "This session is currently being recorded (recording in host browser)",
      "recStart": "Start recording",
      "recStop": "Stop recording"
    },
    "unpin": "Unpin",
    "unpinLabel": "Exit pin ✕",
    "view": {
      "gallery": "Gallery",
      "modeLabel": "View mode",
      "podium": "Podium"
    },
    "you": "You"
  }
}
