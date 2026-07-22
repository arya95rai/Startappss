from collections import deque

class JobScheduler:
    def __init__(self):
        self.pending = deque()
        self.completed = deque()
        self.retry = deque()

    # Add a new job
    def add_job(self, job):
        self.pending.append(job)

    # Process next pending job
    def process_job(self, success=True):
        if not self.pending:
            print("No pending jobs")
            return

        job = self.pending.popleft()

        if success:
            self.completed.append(job)
            print(f"{job} completed")
        else:
            self.retry.append(job)
            print(f"{job} moved to retry queue")

    # Retry failed jobs
    def retry_job(self):
        if not self.retry:
            print("No jobs to retry")
            return

        job = self.retry.popleft()
        self.pending.append(job)
        print(f"{job} moved back to pending queue")

    # Display all queues
    def display(self):
        print("Pending  :", list(self.pending))
        print("Completed:", list(self.completed))
        print("Retry    :", list(self.retry))
        print()


# ---------------- Driver Code ----------------

scheduler = JobScheduler()

scheduler.add_job("Job1")
scheduler.add_job("Job2")
scheduler.add_job("Job3")

scheduler.display()

scheduler.process_job(True)      # Job1 completed
scheduler.process_job(False)     # Job2 failed

scheduler.display()

scheduler.retry_job()

scheduler.display()

scheduler.process_job(True)      # Job3 completed
scheduler.process_job(True)      # Job2 completed

scheduler.display()