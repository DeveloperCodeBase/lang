# Spanish translations for Part 2a: atoms, classes, tables
PART2A_ES = {
  "atoms": {
    "captions": {
      "etaTradeoff": "Si η es demasiado grande, la función de coste diverge; si es muy pequeña, la convergencia es lenta.",
      "fasterNoisier": "Esto hace que las actualizaciones sean más rápidas pero más oscilantes.",
      "lrAnswer": "Buena pregunta. Normalmente se combina con un planificador de tasa de aprendizaje o con Adam.",
      "lrQuestion": "¿Profesor, cómo se selecciona la tasa de aprendizaje óptima para SGD?",
      "sgdStep": "El descenso de gradiente estocástico utiliza solo una muestra por paso para calcular el gradiente."
    },
    "chat": {
      "seed": {
        "answer": "Claro. Supongamos θ = 0.8, gradiente = 2.4 y η = 0.1. Entonces:",
        "answerTime": "14:25",
        "ask": "¿Podría dar un ejemplo numérico de actualización de pesos en SGD?",
        "askTime": "14:25",
        "greeting": "Hola 👋 Soy el asistente inteligente de esta sesión. Puedo resumir en tiempo real, aclarar conceptos o sugerir ejercicios prácticos.",
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
        "name": "Armán B."
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
        "adamWeighted": "Adam con ponderación de clases",
        "rmspropWarmup": "RMSprop con calentamiento (Warm-up)",
        "sgdMomentum": "SGD estándar con momento (Momentum)"
      },
      "question": "¿Qué método de optimización es más adecuado para entrenar redes profundas con datos desbalanceados?"
    },
    "qa": {
      "q1": {
        "text": "Si la función de coste no es convexa, ¿converge SGD a un mínimo global?",
        "time": "Hace 2 minutos"
      },
      "q2": {
        "text": "¿Cómo se equilibra el sesgo y la varianza al ajustar el tamaño del mini-lote?",
        "time": "Hace 5 minutos"
      }
    },
    "session": {
      "title": "Optimización avanzada en aprendizaje profundo",
      "instructor": "Dr. Azimi",
      "date": "Semestre actual"
    }
  },
  "classes": {
    "card": {
      "attendees": "{value, number} participantes",
      "cancelled": "Esta sesión ha sido cancelada.",
      "joinDirect": "Entrada directa",
      "joinLobby": "Entrar a la sala de espera",
      "newTab": "Abrir en nueva pestaña",
      "report": "Informe de sesión",
      "reportTitle": "Informe completo de esta sesión"
    },
    "emptyAll": "Ninguna sesión coincide con tu búsqueda.",
    "emptyHint": "Tan pronto como el profesor la programe, aparecerá aquí.",
    "emptySearch": "No se encontraron sesiones que coincidan con esta búsqueda o filtro.",
    "errLoad": "Error al cargar las sesiones",
    "eyebrow": "Clase en vivo · Centro de sesiones",
    "filter": {
      "all": "Todas",
      "ended": "Finalizadas",
      "live": "En vivo ahora",
      "scheduled": "Programadas"
    },
    "filterAria": "Filtrar sesiones en vivo",
    "form": {
      "applySlot": "Aplicar esta franja horaria",
      "cancel": "Cancelar",
      "close": "Cerrar",
      "course": "Curso asociado",
      "coursePick": "— Seleccionar curso —",
      "courseSearch": "Buscar curso (código o nombre)…",
      "courseSearchAria": "Buscar curso",
      "coursesError": "La lista de cursos no está disponible; inténtalo de nuevo más tarde.",
      "coursesLoading": "Cargando cursos…",
      "date": "Fecha",
      "dateAria": "Fecha de la sesión",
      "datePlaceholder": "Seleccionar fecha de la sesión",
      "desc": "Descripción (opcional)",
      "descPlaceholder": "Temas o notas clave de esta sesión…",
      "end": "Hora de finalización",
      "errCourse": "Por favor, selecciona un curso asociado.",
      "errCreate": "Error al crear la nueva sesión. Por favor, inténtalo de nuevo.",
      "errDate": "Por favor, selecciona una fecha para la sesión.",
      "errTime": "Por favor, introduce horas de inicio y fin válidas.",
      "errTitle": "Por favor, introduce un título para la sesión.",
      "policy": "Política de admisión",
      "section": "Sección/Grupo (opcional)",
      "sectionAll": "— Curso completo (sin grupo específico) —",
      "sectionOption": "Grupo {group, number}",
      "start": "Hora de inicio",
      "submit": "Programar sesión",
      "submitting": "Programando…",
      "title": "Programar sesión de clase en vivo",
      "titleLabel": "Título de la sesión",
      "titlePlaceholder": "ej., Sesión 4: Algoritmos de optimización"
    },
    "heading": "Sesiones de clase en vivo",
    "hostOnly": "Solo el docente o administrador puede programar sesiones.",
    "myStatus": {
      "absent": "Ausente",
      "enrolled": "Inscrito",
      "excused": "Justificado",
      "present": "Presente"
    },
    "newSession": "Nueva sesión de clase",
    "reload": "Recargar",
    "status": {
      "cancelled": "Cancelada",
      "ended": "Finalizada",
      "live": "En curso",
      "scheduled": "Programada"
    }
  },
  "tables": {
    "assign": {
      "balanced": "Automático (equilibrado)",
      "noStudents": "Aún no hay estudiantes en la clase.",
      "pickFor": "Mesa para {name}",
      "random": "Aleatorio",
      "title": "Asignar asientos",
      "unassigned": "Sin asignar"
    },
    "cancel": "Cancelar",
    "confirm": "Sí",
    "countLabel": "Número de nuevas mesas",
    "capacity": "{used, number} de {total, number} personas",
    "capacityLabel": "Capacidad por mesa",
    "create": "Crear mesa",
    "defaultName": "Mesa {index, number}",
    "dissolve": "Disolver mesa",
    "dissolveConfirm": "¿Disolver \"{name}\"? Sus miembros volverán a la clase principal.",
    "duration": {
      "label": "Duración del trabajo en mesas",
      "option": "{count, number} minutos"
    },
    "empty": "Aún no se han creado mesas.",
    "extend": "{count, number} minutos más",
    "limit": "Máximo {count, number} mesas",
    "mediaNote": "Durante el trabajo en mesas, solo tus compañeros de mesa te ven y te escuchan.",
    "memberCount": "{count, number} personas",
    "members": "Compañeros de mesa",
    "nameLabel": "Nombre de la mesa",
    "peekNotice": "El docente está supervisando las mesas",
    "rejected": {
      "empty": "Ninguna mesa tiene miembros.",
      "full": "Esta mesa está llena.",
      "error": "Ocurrió un error; por favor inténtalo de nuevo.",
      "forbidden": "No tienes permiso para esta acción.",
      "invalid": "Solicitud no válida.",
      "limit": "Has alcanzado el número máximo de mesas.",
      "noRound": "El trabajo en mesas no ha comenzado.",
      "notFound": "Esta mesa ya no existe.",
      "roundActive": "Esta acción no se puede realizar mientras el trabajo en mesas esté activo.",
      "selectionLocked": "La selección de mesa está bloqueada por el docente."
    },
    "remaining": "Tiempo restante: {time}",
    "rename": "Renombrar",
    "returnAll": "Regresar a todos",
    "returnAllConfirm": "¿Regresar a todos a la clase principal?",
    "returned": "Todos regresaron a la clase principal.",
    "running": "Trabajo en mesas en progreso",
    "save": "Guardar",
    "select": {
      "action": "Elegir mesa",
      "full": "Llena",
      "hint": "Elige una mesa libre; puedes cambiarte mientras las mesas estén abiertas."
    },
    "start": "Iniciar mesas",
    "stop": "Terminar mesas",
    "title": "Mesas de trabajo colaborativo"
  }
}
