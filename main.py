import init_django_orm  # noqa: F401

from db.models import Race, Skill, Player, Guild

import json


def main() -> None:
    with open("players.json") as f:
        players_data = json.load(f)

    for key, value in players_data.items():
        race = Race.objects.create(
            name=value["race"]["name"],
            description=value["race"]["description"]
        )
        for skill in value["race"]["skills"]:
            skills = Skill.objects.create(
                name=skill["name"],
                bonus=skill["bonus"],
                race=race,
            )

        guild = Guild.objects.create(
            name=value["guild"]["name"],
            description=value["guild"]["description"],
        )

        player = Player.objects.create(
            nickname=key,
            email=value["email"],
            bio=value["bio"],
            race=race,
            guild=guild,
        )

    print(race, skills, guild, player)


if __name__ == "__main__":
    main()
