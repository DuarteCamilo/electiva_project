"""Models for the application using Peewee ORM."""

from peewee import (
    Model,
    AutoField,
    CharField,
    TextField,
    FloatField,
    IntegerField,
    DateField,
    DateTimeField,
    BooleanField,
    ForeignKeyField,
    MySQLDatabase,
)
from config.settings import DATABASE

print(DATABASE)

database = MySQLDatabase(
    DATABASE["name"],
    user=DATABASE["user"],
    passwd=DATABASE["password"],
    host=DATABASE["host"],
    port=DATABASE["port"],
)

# pylint: disable=too-few-public-methods
class UserModel(Model):
    """User model representing a user in the system."""
    id = AutoField(primary_key=True)
    username = CharField(max_length=50)
    email = CharField(max_length=50)
    password_hash = CharField(max_length=100)

    class Meta:
        """Meta class to define database connection and table name."""
        database = database
        table_name = "users"

class GroupModel(Model):
    """Group model representing a user group."""
    id = AutoField(primary_key=True)
    name = CharField(max_length=50)

    class Meta:
        """Meta class to define database connection and table name."""
        database = database
        table_name = "groups"

class IngredientCategoryModel(Model):
    """Ingredient category model."""
    id = AutoField(primary_key=True)
    name = CharField(max_length=50)

    class Meta:
        """Meta class to define database connection and table name."""
        database = database
        table_name = "ingredient_categories"

class UnitModel(Model):
    """Unit model for measurement units."""
    id = AutoField(primary_key=True)
    name = CharField(max_length=50)

    class Meta:
        """Meta class to define database connection and table name."""
        database = database
        table_name = "units"

class IngredientModel(Model):
    """Ingredient model representing a specific ingredient."""
    id = AutoField(primary_key=True)
    name = CharField(max_length=50)
    category_id = ForeignKeyField(IngredientCategoryModel, backref='ingredients')
    unit_id = ForeignKeyField(UnitModel, backref='ingredients')

    class Meta:
        """Meta class to define database connection and table name."""
        database = database
        table_name = "ingredients"

class NotificationModel(Model):
    """Model representing notifications for users."""
    id = AutoField(primary_key=True)
    user_id = ForeignKeyField(UserModel, backref='notifications')
    message = TextField()
    created_at = DateTimeField()
    is_read = BooleanField()

    class Meta:
        """Meta class to define database connection and table name."""
        database = database
        table_name = "notifications"

class MenuModel(Model):
    """Menu model representing a user-created menu."""
    id = AutoField(primary_key=True)
    name = CharField(max_length=50)
    user_id = ForeignKeyField(UserModel, backref='menus')
    start_date = DateField()
    end_date = DateField()

    class Meta:
        """Meta class to define database connection and table name."""
        database = database
        table_name = "menus"

class PantryItemModel(Model):
    """Model representing items in a user's pantry."""
    id = AutoField(primary_key=True)
    quantity = FloatField()
    unit_id = ForeignKeyField(UnitModel, backref='pantry_items')
    expiry_date = DateField()
    user_id = ForeignKeyField(UserModel, backref='pantry_items')
    ingredient_id = ForeignKeyField(IngredientModel, backref='pantry_items')

    class Meta:
        """Meta class to define database connection and table name."""
        database = database
        table_name = "pantry_items"

class RecipeTypeModel(Model):
    """Model representing types of recipes."""
    id = AutoField(primary_key=True)
    name = CharField(max_length=50)

    class Meta:
        """Meta class to define database connection and table name."""
        database = database
        table_name = "recipe_types"

class RecipeModel(Model):
    """Model representing a recipe."""
    id = AutoField(primary_key=True)
    name = CharField(max_length=50)
    description = TextField()
    instructions = TextField()
    preparation_time = IntegerField()
    datosNutricionales = TextField()
    type_id = ForeignKeyField(RecipeTypeModel, backref='recipes')
    difficulty = CharField(max_length=50)
    is_public = BooleanField()
    user_id = ForeignKeyField(UserModel, backref='recipes')

    class Meta:
        """Meta class to define database connection and table name."""
        database = database
        table_name = "recipes"

class FavoriteRecipeModel(Model):
    """Model representing a user's favorite recipes."""
    id = AutoField(primary_key=True)
    user_id = ForeignKeyField(UserModel, backref='favorite_recipes')
    recipe_id = ForeignKeyField(RecipeModel, backref='favorite_recipes')

    class Meta:
        """Meta class to define database connection and table name."""
        database = database
        table_name = "favorite_recipes"

class MenuRecipeModel(Model):
    """Model representing recipes in a menu."""
    id = AutoField(primary_key=True)
    menu_id = ForeignKeyField(MenuModel, backref='menu_recipes')
    recipe_id = ForeignKeyField(RecipeModel, backref='menu_recipes')
    meal_time = CharField(max_length=50)
    planned_date = DateField()

    class Meta:
        """Meta class to define database connection and table name."""
        database = database
        table_name = "menu_recipes"

class RecipeRecipeTypeModel(Model):
    """Model for linking recipes and recipe types."""
    id = AutoField(primary_key=True)
    recipe_id = ForeignKeyField(RecipeModel, backref='recipe_recipe_types', on_delete='CASCADE')
    type_id = ForeignKeyField(RecipeTypeModel, backref='recipe_recipe_types', on_delete='CASCADE')

    class Meta:
        """Meta class to define database connection and table name."""
        database = database
        table_name = "recipe_recipe_types"

class RecipeIngredientModel(Model):
    """Model representing ingredients used in a recipe."""
    id = AutoField(primary_key=True)
    recipe_id = ForeignKeyField(RecipeModel, backref='recipe_ingredients')
    ingredient_id = ForeignKeyField(IngredientModel, backref='recipe_ingredients')
    quantity = FloatField()
    unit_id = ForeignKeyField(UnitModel, backref='recipe_ingredients')

    class Meta:
        """Meta class to define database connection and table name."""
        database = database
        table_name = "recipe_ingredients"

class ShoppingListModel(Model):
    """Model representing a shopping list for a user."""
    id = AutoField(primary_key=True)
    name = CharField(max_length=50)
    created_at = DateTimeField()
    user_id = ForeignKeyField(UserModel, backref='shopping_lists')

    class Meta:
        """Meta class to define database connection and table name."""
        database = database
        table_name = "shopping_lists"

class ShoppingListItemModel(Model):
    """Model representing items in a shopping list."""
    id = AutoField(primary_key=True)
    shopping_list_id = ForeignKeyField(ShoppingListModel, backref='shopping_list_items')
    ingredient_id = ForeignKeyField(IngredientModel, backref='shopping_list_items')
    quantity = FloatField()
    unit_id = ForeignKeyField(UnitModel, backref='shopping_list_items')
    is_purchased = BooleanField()

    class Meta:
        """Meta class to define database connection and table name."""
        database = database
        table_name = "shopping_list_items"

class UserGroupModel(Model):
    """Model for linking users and groups."""
    id = AutoField(primary_key=True)
    user_id = ForeignKeyField(UserModel, backref='user_groups', on_delete='CASCADE')
    group_id = ForeignKeyField(GroupModel, backref='user_groups', on_delete='CASCADE')

    class Meta:
        """Meta class to define database connection and table name."""
        database = database
        table_name = "user_groups"
