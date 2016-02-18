import setuptools

setuptools.setup(
    name="emote",
    version="0.1.0",
    packages=setuptools.find_packages(),
    include_package_data=True,
    author="Danielle Jenkins",
    author_email="d@d6e.io",
    description="A simple emote tool for quickly fetching common emoticon/emoji.",
    install_requires=['pyperclip'],
    url="https://github.com/d6e/emote",
    entry_points={
            "console_scripts": ["emote = emote:parse_cli"],
    }
)
