TOOLS = {

    "filesystem": {
        "description": "Check filesystem usage",
        "command": "df -h"
    },

    "memory": {
        "description": "Check memory usage",
        "command": "free -h"
    },

    "cpu": {
        "description": "Check CPU usage",
        "command": "top -bn1 | head -20"
    },

    "hostname": {
        "description": "Get hostname",
        "command": "hostname"
    }

}