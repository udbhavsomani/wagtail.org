# Generated by Django 3.2.12 on 2022-08-22 14:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("taxonomy", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="category",
            name="icon",
            field=models.CharField(
                blank=True,
                choices=[
                    ("arrow-alt", "Arrow alt"),
                    ("arrow-in-circle", "Arrow in circle"),
                    ("arrow-in-square", "Arrow in square"),
                    ("arrows", "Arrows"),
                    ("blog", "Blog"),
                    ("bread", "Bread"),
                    ("briefcase", "Briefcase"),
                    ("building", "Building"),
                    ("calendar", "Calendar"),
                    ("code-file", "Code File"),
                    ("document", "Document"),
                    ("envelope", "Envelope"),
                    ("explanation", "Explanation"),
                    ("eye", "Eye"),
                    ("flame", "Flame"),
                    ("friends", "Friends"),
                    ("github", "Github"),
                    ("handshake", "Handshake"),
                    ("heart", "Heart"),
                    ("history", "History"),
                    ("id-card", "ID Card"),
                    ("image", "Image"),
                    ("knife-fork", "Knife Fork"),
                    ("leaf", "Leaf"),
                    ("location-pin", "Location Pin"),
                    ("map", "Map"),
                    ("magnifying-glass", "Magnifying Glass"),
                    ("money", "Money"),
                    ("moon", "Moon"),
                    ("one-two-steps", "One Two Steps"),
                    ("padlock", "Padlock"),
                    ("paper-plane", "Paper Plane"),
                    ("paper-stack", "Paper Stack"),
                    ("pen-checkbox", "Pen Checkbox"),
                    ("person-in-tie", "Person in Tie"),
                    ("python", "Python"),
                    ("question-mark-circle", "Question Mark Circle"),
                    ("quotes", "Quotes"),
                    ("release-cycle", "Release Cycle"),
                    ("roadmap", "Roadmap"),
                    ("rocket", "Rocket"),
                    ("rollback", "Rollback"),
                    ("slack", "Slack"),
                    ("speech-bubble", "Speech Bubble"),
                    ("sun-cloud", "Sun Cloud"),
                    ("table-tennis", "Table Tennis"),
                    ("tree", "Tree"),
                    ("wordpress", "Wordpress"),
                    ("world", "World"),
                ],
                max_length=255,
            ),
        ),
    ]
