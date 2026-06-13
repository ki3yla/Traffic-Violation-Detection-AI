from dataclasses import dataclass
from datetime import datetime

@dataclass
class TrafficReport:
    id: str
    image_path: str
    violation_type: str
    timestamp: datetime

global_reports = []