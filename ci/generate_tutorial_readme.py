import os
from glob import glob


def main():

    readme_text = [
        "# Neuromatch Academy Tutorial Notebooks",
        "",
    ]

    day_paths = sorted(glob("tutorials/W?D?_*"))
    for day_path in day_paths:

        day_name = os.path.split(day_path)[-1]
        day_code, topic = day_name.split("_")

        topic_words = []
        for letter in topic:
            if letter.isupper():
                topic_words.append(letter)
            else:
                topic_words[-1] += letter
        topic = " ".join(topic_words)

        # Note: this will fail if we have 10 notebooks
        notebooks = sorted(glob(f"{day_path}/*.ipynb"))

        if not notebooks:
            continue

        readme_text.extend([
            f"## {day_code} - {topic}",
            "",
            "|   | Student version | Instructor version |",
            "| - | --------------- | ------------------ |",
        ])

        for i, instructor_nb in enumerate(notebooks, 1):
            _, nb_fname = os.path.split(instructor_nb)
            student_nb = f"{day_path}/student/{nb_fname}"

            student_badge = make_colab_badge(student_nb)
            instructor_badge = make_colab_badge(instructor_nb)

            readme_text.append(
                f"| Tutorial {i} | {student_badge} | {instructor_badge} |"
            )

        readme_text.append("\n")

    with open("tutorials/README.md", "w") as f:

        f.write("\n".join(readme_text))


def make_colab_badge(github_path):

    alt_text = "Open In Colab"
    badge_svg = "https://colab.research.google.com/assets/colab-badge.svg"
    url_base = (
        "https://colab.research.google.com/"
        "github/NeuromatchAcademy/course-content/blob/master/"
    )
    return make_badge(alt_text, badge_svg, url_base, github_path)


def make_nbviewer_badge(github_path):

    alt_text = "View the notebook"
    badge_svg = "https://img.shields.io/badge/render-nbviewer-orange.svg"
    url_base = (
        "https://nbviewer.jupyter.org/"
        "github/NeuromatchAcademy/course-content/blob/master/"
    )
    return make_badge(alt_text, badge_svg, url_base, github_path)


def make_badge(alt_text, badge_svg, url_base, github_path):

    return f"[![{alt_text}]({badge_svg})]({url_base}/{github_path})"


if __name__ == "__main__":

    main()
