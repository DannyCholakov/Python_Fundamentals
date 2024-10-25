class Catalogue:
    def __init__(self, name: str):
        self.name = name
        self.products = []

    def add_product(self, product_name: str):
        self.products.append(product_name)

    def get_by_letter(self, first_letter: str):
        # Use a list comprehension to filter products by the first letter
        return [product for product in self.products if product[0] == first_letter]

    def __repr__(self):
        # Display catalogue name and sorted product list
        sorted_products = '\n'.join(sorted(self.products))
        return f"Items in the {self.name} catalogue:\n{sorted_products}"
