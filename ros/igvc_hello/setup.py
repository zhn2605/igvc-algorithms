from setuptools import find_packages, setup

package_name = "igvc_hello"

setup(
    name=package_name,
    version="0.0.0",
    packages=find_packages(exclude=["test"]),
    data_files=[
        ("share/ament_index/resource_index/packages", ["resource/" + package_name]),
        ("share/" + package_name, ["package.xml"]),
    ],
    install_requires=["setuptools"],
    zip_safe=True,
    maintainer="zhn",
    maintainer_email="zzihan0805@gmail.com",
    description="Smoke test: a ROS node that imports a core package through the venv bridge.",
    license="Apache-2.0",
    extras_require={
        "test": [
            "pytest",
        ],
    },
    entry_points={
        "console_scripts": ["hello = igvc_hello.hello:main"],
    },
)
