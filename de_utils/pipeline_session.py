from datetime import datetime


class PipelineSession:
    """
    Track the start and completion of a data pipeline run.
    """

    def __init__(self, pipeline_name: str):
        self.pipeline_name = pipeline_name
        self.start_time = None
        self.end_time = None

    def start(self):
        self.start_time = datetime.now()
        print(f"{self.pipeline_name} started at {self.start_time}")

    def end(self):
        self.end_time = datetime.now()
        print(f"{self.pipeline_name} completed at {self.end_time}")

    def duration(self):
        if self.start_time is None or self.end_time is None:
            return None

        return self.end_time - self.start_time
