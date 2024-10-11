import datetime
from sqlalchemy import Boolean, Column, Date, DateTime, Float, Integer, String, ForeignKey, Text, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from config.settings import DATABASE

Base = declarative_base()

class UserModel(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(50), unique=True, index=True)
    email = Column(String(50), unique=True, index=True)
    password_hash = Column(String(100))

class GroupModel(Base):
    __tablename__ = "groups"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(50))

class IngredientCategoryModel(Base):
    __tablename__ = "ingredient_categories"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(50))

class UnitModel(Base):
    __tablename__ = "units"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(50))

class IngredientModel(Base):
    __tablename__ = "ingredients"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(50), index=True)
    category_id = Column(Integer, ForeignKey('ingredient_categories.id'))
    unit_id = Column(Integer, ForeignKey('units.id'))


class NotificationModel(Base):
    __tablename__ = "notifications"
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    message = Column(String(200))
    created_at = Column(DateTime)
    is_read = Column(Boolean)

class MenuModel(Base):
    __tablename__ = "menus"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(50), index=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    start_date = Column(Date)
    end_date = Column(Date)

class PantryItemModel(Base):
    __tablename__ = "pantry_items"
    id = Column(Integer, primary_key=True, index=True)
    quantity = Column(Float)
    unit_id = Column(Integer, ForeignKey('units.id'))
    expiry_date = Column(Date)
    user_id = Column(Integer, ForeignKey('users.id'))
    ingredient_id = Column(Integer, ForeignKey('ingredients.id'))

class RecipeTypeModel(Base):
    __tablename__ = "recipe_types"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(50))

class RecipeModel(Base):
    __tablename__ = "recipes"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(50))
    description = Column(Text)
    instructions = Column(Text)
    preparation_time = Column(Integer)
    datosNutricionales = Column(Text)
    type_id = Column(Integer, ForeignKey('recipe_types.id'))
    difficulty = Column(String(50))
    is_public = Column(Boolean)
    user_id = Column(Integer, ForeignKey('users.id'))

class FavoriteRecipeModel(Base):
    __tablename__ = "favorite_recipes"
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    recipe_id = Column(Integer, ForeignKey('recipes.id'))

class MenuRecipeModel(Base):
    __tablename__ = "menu_recipes"
    id = Column(Integer, primary_key=True, index=True)
    menu_id = Column(Integer, ForeignKey('menus.id'))
    recipe_id = Column(Integer, ForeignKey('recipes.id'))
    meal_time = Column(String(50))
    planned_date = Column(Date)

class RecipeRecipeTypeModel(Base):
    __tablename__ = "recipe_recipe_types"
    id = Column(Integer, primary_key=True, index=True)
    recipe_id = Column(Integer, ForeignKey('recipes.id'))
    type_id = Column(Integer, ForeignKey('recipe_types.id'))

class RecipeIngredientModel(Base):
    __tablename__ = "recipe_ingredients"
    id = Column(Integer, primary_key=True, index=True)
    recipe_id = Column(Integer, ForeignKey('recipes.id'))
    ingredient_id = Column(Integer, ForeignKey('ingredients.id'))
    quantity = Column(Float)
    unit_id = Column(Integer, ForeignKey('units.id'))

class ShoppingListModel(Base):
    __tablename__ = "shopping_lists"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(50))
    created_at = Column(DateTime)
    user_id = Column(Integer, ForeignKey('users.id'))

class ShoppingListItemModel(Base):
    __tablename__ = "shopping_list_items"
    id = Column(Integer, primary_key=True, index=True)
    shopping_list_id = Column(Integer, ForeignKey('shopping_lists.id'))
    ingredient_id = Column(Integer, ForeignKey('ingredients.id'))
    quantity = Column(Float)
    unit_id = Column(Integer, ForeignKey('units.id'))
    is_purchased = Column(Boolean)

class UserGroupModel(Base):
    __tablename__ = "user_groups"
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    group_id = Column(Integer, ForeignKey('groups.id'))

# Configurar la base de datos
DATABASE_URL = f"mysql+pymysql://{DATABASE['user']}:{DATABASE['password']}@{DATABASE['host']}/{DATABASE['name']}"
engine = create_engine(DATABASE_URL)


# Crear una sesión de base de datos
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

#Base.metadata.create_all(engine)    -----> para cargar tablas