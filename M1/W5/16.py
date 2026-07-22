from collections import deque

class UndoRedo:
    def __init__(self):
        self.undo_stack = deque()
        self.redo_stack = deque()

    def perform(self, action):
        self.undo_stack.append(action)
        self.redo_stack.clear()

    def undo(self):
        if not self.undo_stack:
            print("Nothing to undo")
            return

        action = self.undo_stack.pop()
        self.redo_stack.append(action)
        print("Undo:", action)

    def redo(self):
        if not self.redo_stack:
            print("Nothing to redo")
            return

        action = self.redo_stack.pop()
        self.undo_stack.append(action)
        print("Redo:", action)

    def current_state(self):
        print("Actions:", list(self.undo_stack))


# ---------------- Driver Code ----------------

editor = UndoRedo()

editor.perform("Type A")
editor.perform("Type B")
editor.perform("Type C")

editor.current_state()

editor.undo()
editor.current_state()

editor.undo()
editor.current_state()

editor.redo()
editor.current_state()

editor.perform("Type D")
editor.current_state()

editor.redo()