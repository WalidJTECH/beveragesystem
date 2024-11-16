
class Drink:
    """Class to represent a drink with a single base and multiple flavors."""

    # Valid bases and flavors for drinks
    _valid_bases = ['water', 'sbrite', 'pokeacola', 'Mr. Salt', 'hill fog', 'leaf wine']
    _valid_flavors = ['lemon', 'cherry', 'strawberry', 'mint', 'blueberry', 'lime']

    def __init__(self):
        """Initialize a drink with no base and no flavors."""
        self._base = None  # Base of the drink (e.g., water, sbrite)
        self._flavors = set()  # Set to store unique flavors added to the drink

    def get_base(self):
        """Retrieve the base of the drink.

        Returns:
            str: The base of the drink.
        """
        return self._base

    def get_flavors(self):
        """Retrieve the list of flavors added to the drink.

        Returns:
            list: List of flavors added to the drink.
        """
        return list(self._flavors)

    def get_num_flavors(self):
        """Count the number of flavors in the drink.

        Returns:
            int: Number of unique flavors added.
        """
        return len(self._flavors)

    def add_base(self, base):
        """Add a base to the drink.

        Args:
            base (str): The base to be added.

        Raises:
            ValueError: If a base is already set or the base is not valid.
        """
        if self._base is not None:
            raise ValueError("A base has already been added.")
        if base not in self._valid_bases:
            raise ValueError(f"Invalid base: {base}. Valid options: {self._valid_bases}")
        self._base = base

    def add_flavor(self, flavor):
        """Add a flavor to the drink.

        Args:
            flavor (str): The flavor to be added.

        Raises:
            ValueError: If the flavor is not valid or already added.
        """
        if flavor not in self._valid_flavors:
            raise ValueError(f"Invalid flavor: {flavor}. Valid options: {self._valid_flavors}")
        if flavor in self._flavors:
            raise ValueError(f"Flavor '{flavor}' has already been added.")
        self._flavors.add(flavor)

    def set_flavors(self, flavors):
        """Replace all current flavors with a new set of flavors.

        Args:
            flavors (list): List of flavors to add to the drink.

        Raises:
            ValueError: If any flavor in the list is invalid.
        """
        self._flavors.clear()
        for flavor in flavors:
            self.add_flavor(flavor)


class Order:
    """Class to manage a collection of drink orders."""

    def __init__(self):
        """Initialize an empty order with no items."""
        self._items = []  # List to store all drinks in the order

    def get_items(self):
        """Retrieve all items in the order.

        Returns:
            list: List of all Drink objects in the order.
        """
        return self._items

    def get_num_items(self):
        """Count the number of drinks in the order.

        Returns:
            int: Number of drinks in the order.
        """
        return len(self._items)

    def get_total(self):
        """Calculate the total cost of the order.

        Returns:
            float: Total cost of the order based on $5 per drink.
        """
        price_per_drink = 5.00  # Fixed price per drink
        return len(self._items) * price_per_drink

    def get_receipt(self):
        """Generate a detailed receipt for the order.

        Returns:
            str: Formatted receipt showing all drinks and total cost.
        """
        if not self._items:
            return "Order is empty. Add some drinks!"
        
        receipt_lines = ["--- Order Receipt ---"]
        for idx, drink in enumerate(self._items, 1):
            receipt_lines.append(
                f"{idx}. Base: {drink.get_base()}, Flavors: {', '.join(drink.get_flavors()) or 'None'}"
            )
        receipt_lines.append(f"Total Drinks: {self.get_num_items()}")
        receipt_lines.append(f"Total Cost: ${self.get_total():.2f}")
        return "\n".join(receipt_lines)

    def add_item(self, drink):
        """Add a drink to the order.

        Args:
            drink (Drink): The drink to add to the order.

        Raises:
            TypeError: If the provided item is not a Drink object.
        """
        if not isinstance(drink, Drink):
            raise TypeError("Invalid item. Only Drink objects are allowed.")
        self._items.append(drink)

    def remove_item(self, index):
        """Remove a drink from the order by its index.

        Args:
            index (int): Index of the drink to remove.

        Raises:
            IndexError: If the index is invalid.
        """
        if index < 0 or index >= len(self._items):
            raise IndexError("Invalid index. No drink removed.")
        self._items.pop(index)
