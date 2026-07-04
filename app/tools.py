TOOLS = {
    "filesystem": {
        "command": "df -h",
        "description": "Check filesystem usage",
        "keywords": ["filesystem", "disk", "storage", "space"]
    },

    "memory": {
        "command": "free -h",
        "description": "Check memory usage",
        "keywords": ["memory", "ram"]
    },

    "cpu": {
        "command": "top -bn1 | head -20",
        "description": "Check CPU usage",
        "keywords": ["cpu", "processor", "load"]
    },

    "hostname": {
        "command": "hostname",
        "description": "Get hostname",
        "keywords": ["hostname", "host", "server name"]
    }
}