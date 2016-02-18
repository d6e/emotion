import setuptools
import emote

setuptools.setup(
    name="emotion",
    version="0.1.0",
    packages=setuptools.find_packages(),
    include_package_data=True,
    author="Danielle Jenkins",
    author_email="d@d6e.io",
    description=emote.__doc__,
    install_requires=['pyperclip'],
    url="https://github.com/d6e/emotion",
    entry_points={
        "console_scripts": ["emotion = emote.emote:main"],
    }
)
