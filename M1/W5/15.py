from collections import deque

class BrowserHistory:
    def __init__(self):
        self.back_history = deque()
        self.forward_history = deque()
        self.current = None

    def visit(self, page):
        if self.current is not None:
            self.back_history.append(self.current)

        self.current = page
        self.forward_history.clear()

    def back(self):
        if not self.back_history:
            print("No previous page")
            return

        self.forward_history.appendleft(self.current)
        self.current = self.back_history.pop()

    def forward(self):
        if not self.forward_history:
            print("No next page")
            return

        self.back_history.append(self.current)
        self.current = self.forward_history.popleft()

    def current_page(self):
        print("Current Page:", self.current)


# ---------------- Driver Code ----------------

browser = BrowserHistory()

browser.visit("google.com")
browser.visit("youtube.com")
browser.visit("github.com")

browser.current_page()

browser.back()
browser.current_page()

browser.back()
browser.current_page()

browser.forward()
browser.current_page()

browser.visit("chatgpt.com")
browser.current_page()

browser.forward()