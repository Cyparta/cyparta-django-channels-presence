from django import dispatch

presence_changed = dispatch.Signal(
    #providing_args=["room", "added", "removed", "bulk_change"] # moaz and eslam comment this line rabna youster
)
