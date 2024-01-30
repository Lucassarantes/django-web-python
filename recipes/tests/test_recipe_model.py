from .test_recipe_base import RecipeTestBase
from django.core.exceptions import ValidationError
from parameterized import parameterized
from recipe import models


class RecipeModelTest(RecipeTestBase):
    def setUp(self) -> None:
        self.recipe = self.make_recipe()
        return super().setUp()

    def make_recipe_no_defaults(self):
        recipe = models.Recipe(
            category_data=self.make_category(name="test_default_category"),
            author_data=self.make_author(username="newuser_"),
            title='Recipe Title',
            description='Recipe Description',
            slug='recipe-slug',
            preparation_time=10,
            preparation_time_unit='Minutes',
            servings=5,
            servings_unit='Portions',
            preparation_steps='Recipe Preparation Steps',
            preparation_steps_is_html=False,
            is_published=True,
            cover="recipes/images/et.png"
        )
        recipe.full_clean()
        recipe.save()
        return recipe

    def test_recipe_title_raises_error_if_title_has_more_than_65_chars(self):
        self.recipe.title = "A" * 70
        with self.assertRaises(ValidationError):
            self.recipe.full_clean()

    @parameterized.expand([
        ('title', 65),
        ('description', 65),
        ('preparation_time_unit', 65),
        ('servings_unit', 65)
    ])
    def test_recipe_fields_max_length(self, field, max_length):
        setattr(self.recipe, field, 'A' * (max_length + 1))
        with self.assertRaises(ValidationError):
            self.recipe.full_clean()

    def test_recipe_preparation_steps_is_html_is_false_by_default(self):
        recipe = self.make_recipe_no_defaults()
        recipe.full_clean()
        recipe.save()
        self.assertFalse(recipe.preparation_steps_is_html,
                         msg="Recipe preparation_steps_is_html is not False")

    def test_recipe_is_published_is_false_by_default(self):
        recipe = self.make_recipe_no_defaults()
        recipe.full_clean()
        recipe.save()
        self.assertFalse(recipe.preparation_steps_is_html,
                         msg="Recipe is_published is not False")
