import json

with open('locales/fa/live.json') as fp:
    fa_live = json.load(fp)

import scripts.live_part1 as p1
import scripts.live_part2a as p2a
import scripts.live_part2b as p2b
import scripts.live_part2c as p2c

en_tree = {}
en_tree.update(p1.PART1)
en_tree.update(p2a.PART2A)
en_tree.update(p2b.PART2B)
en_tree.update(p2c.PART2C)

missing_map = {
  "classes.form.cancel": "Cancel",
  "classes.form.close": "Close",
  "classes.form.course": "Associated course",
  "classes.form.coursePick": "— Select course —",
  "classes.form.courseSearch": "Search course (code or name)…",
  "classes.form.courseSearchAria": "Search course",
  "classes.form.coursesError": "Course list is unavailable; please try again later.",
  "classes.form.coursesLoading": "Loading courses…",
  "classes.form.date": "Date",
  "classes.form.dateAria": "Session date",
  "classes.form.datePlaceholder": "Select session date",
  "classes.form.desc": "Description (optional)",
  "classes.form.descPlaceholder": "Topics or key notes for this session…",
  "classes.form.end": "End time",
  "classes.form.errCourse": "Please select an associated course.",
  "classes.form.errCreate": "Failed to create new session. Please try again.",
  "classes.form.errDate": "Please select a session date.",
  "classes.form.errTime": "Please enter valid start and end times.",
  "classes.form.errTitle": "Please enter a session title.",
  "classes.form.policy": "Admission policy",
  "classes.form.section": "Section/Class (optional)",
  "classes.form.sectionAll": "— Whole course (no specific section) —",
  "classes.form.sectionOption": "Section {group, number}",
  "classes.form.start": "Start time",
  "classes.form.submit": "Schedule session",
  "classes.form.submitting": "Scheduling…",
  "classes.form.title": "Schedule Live Class Session",
  "classes.form.titleLabel": "Session title",
  "classes.form.titlePlaceholder": "e.g., Chapter 3 Problem Solving",
  "classes.group.live": "Live Now",
  "classes.group.liveEmpty": "No sessions are currently live.",
  "classes.group.past": "Past",
  "classes.group.pastEmpty": "No past sessions recorded.",
  "classes.group.upcoming": "Upcoming",
  "classes.group.upcomingEmpty": "No upcoming sessions scheduled.",
  "classes.help.body": "On this page, you can see live classes categorized as \"Live Now\", \"Upcoming\", and \"Past\". Click \"Enter Lobby\" to test your camera and microphone before entering; if a session is currently live, click \"Direct Entry\" to join immediately. Instructors and administrators can schedule a new live class with \"New Session\".",
  "classes.help.title": "Live Classes Guide",
  "guide.lobby.chain.schedule": "The live class is scheduled in the syllabus and appears in \"My Classes\".",
  "guide.lobby.roles.support.does": "If device tests repeatedly fail, technical support uses this readiness report for troubleshooting.",
  "guide.lobby.roles.support.label": "Technical Support",
  "guide.lobby.youCan.camera": "View camera preview and toggle it on/off; when off, your avatar is displayed.",
  "guide.lobby.youCan.join": "Once the readiness checklist turns green, join using the Enter Class button.",
  "guide.lobby.youCan.name": "Edit your display name before entering class.",
  "guide.sections.chain": "Full journey, from start to finish",
  "guide.sections.ifEmpty": "If the page is empty",
  "guide.sections.roles": "Who does what",
  "guide.sections.youCan": "What can you do here?",
  "report.engagement.handsTitle": "Hands raised",
  "report.engagement.notCaptured": "Interactive artifacts were not recorded for this session (closed without host \"End Session\" or no live interaction occurred).",
  "report.engagement.polls": "Polls:",
  "report.engagement.timelineTitle": "Timeline",
  "report.kpi.absent": "Absent",
  "report.kpi.actualMinutes": "Actual session duration",
  "report.kpi.chatCount": "Chat messages",
  "report.kpi.joins": "Join count",
  "report.kpi.myMinutes": "My attendance duration",
  "report.kpi.myStatus": "My attendance status",
  "report.kpi.participants": "Participants",
  "report.kpi.presentIncLate": "Present (including late)",
  "report.kpi.scheduledMinutes": "Scheduled duration",
  "report.kpi.totalMinutes": "Total attendance minutes",
  "report.poll.ended": "Ended",
  "report.poll.multi": " · Multiple choice",
  "report.poll.open": "Open",
  "report.poll.total": "Total votes: {value, number}",
  "session.captions.unavailableHere": "Captions not available in this browser",
  "session.captions.unsupported": "Your browser does not support live transcription (Chrome/Edge)",
  "session.diag.available": "Available ✓",
  "session.diag.browser": "Browser",
  "session.diag.engine": "Engine",
  "session.diag.engineNative": "Native browser",
  "session.diag.engineNone": "❌ None",
  "session.diag.engineServer": "Server",
  "session.diag.hint": "If \"Audio Level\" does not move when speaking, the browser is not delivering microphone audio to the page.",
  "session.diag.lastError": "Last error",
  "session.diag.level": "Audio level",
  "session.diag.listening": "Listening ✓",
  "session.diag.mic": "Microphone",
  "session.diag.micOff": "Off ❌",
  "session.diag.micOn": "On ✓",
  "session.diag.off": "Off",
  "session.diag.restarts": "Start attempts",
  "session.diag.speech": "Browser speech recognition",
  "session.diag.starting": "Starting…",
  "session.diag.status": "🛈 Caption status:",
  "session.diag.unavailable": "Not available ❌",
  "session.download.formatMenu": "Download format",
  "session.download.label": "Download",
  "session.download.loading": "Downloading…",
  "session.download.srt": "Subtitles (.srt)",
  "session.download.vtt": "WebVTT (.vtt)",
  "session.end.confirmBody": "Once confirmed, you will have 10 seconds to cancel ending the class; then all participants will be disconnected.",
  "session.end.confirmCta": "End class for everyone",
  "session.end.confirmTitle": "End class for all participants?",
  "session.end.pendingHost": "Class will end in {seconds} seconds.",
  "session.end.pendingStudent": "Instructor is ending the class.",
  "session.end.undo": "Cancel ending class",
  "session.end.undoFailed": "Cancellation window has expired. To continue, create a new session.",
  "session.ended.byHost": "Class ended by instructor",
  "session.ended.forAll": "Class ended for everyone",
  "session.ended.redirecting": "Redirecting to live class list…",
  "session.film.emptyHint": "As others join, each participant's tile will appear here.",
  "session.film.emptyTitle": "No one has joined yet",
  "session.film.regionLabel": "Participants",
  "session.fs.enterLabel": "Fullscreen ⛶",
  "session.jitsi.loadFailed": "Failed to load video room. Check internet connection or Jitsi domain, or use the button below to open session in a new tab.",
  "session.jitsi.openNewTab": "Open session in new tab"
}

def set_path(d, path, val):
    parts = path.split('.')
    cur = d
    for p in parts[:-1]:
        if p not in cur or not isinstance(cur[p], dict):
            cur[p] = {}
        cur = cur[p]
    cur[parts[-1]] = val

for path, val in missing_map.items():
    set_path(en_tree, path, val)

# Remove extra keys by copying strictly the structure of fa_live
def build_matching_tree(fa_sub, en_sub, path=''):
    if isinstance(fa_sub, dict):
        res = {}
        for k, v in fa_sub.items():
            subpath = f'{path}.{k}' if path else k
            en_val = en_sub.get(k) if isinstance(en_sub, dict) else None
            res[k] = build_matching_tree(v, en_val, subpath)
        return res
    else:
        if en_sub is not None and isinstance(en_sub, (str, int, float, bool)):
            return en_sub
        else:
            print(f'Warning: Missing translation for leaf {path}')
            return fa_sub

final_en = build_matching_tree(fa_live, en_tree)

def get_keys(d, prefix=''):
    s = set()
    for k, v in d.items():
        p = f'{prefix}.{k}' if prefix else k
        if isinstance(v, dict):
            s.update(get_keys(v, p))
        else:
            s.add(p)
    return s

fa_k = get_keys(fa_live)
final_k = get_keys(final_en)

assert fa_k == final_k, f'Mismatch: diff={fa_k.symmetric_difference(final_k)}'

with open('locales/en/live.json', 'w', encoding='utf-8') as out:
    json.dump(final_en, out, ensure_ascii=False, indent=2)

print('locales/en/live.json successfully written with exact 1091 keys matching fa!')
