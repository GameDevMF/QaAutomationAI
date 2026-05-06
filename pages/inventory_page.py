class InventoryPage:
    def __init__(self, page):
        self.page = page
        self.inventory_list = ".inventory_list"

    def is_loaded(self):
        return self.page.locator(self.inventory_list).is_visible()
    
    def get_inventory_count(self):
        return len(self.page.locator(".inventory_item").all())
