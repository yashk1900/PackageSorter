# PackageSorter
## How to run
1. Import the sort function from package_sorter
`import package_sorter`
`from package_sorter import sort`
2. Call the `sort(width, height, length, mass)` function, with 4 vairables: width, height, length and mass. (Note: units are centimeters for the dimensions and kilogram for the mass)
3. The function returns type of package based on the given dimension.
4. To run the tests, within your directory, run `python run test_package_sorter.py`
## Business logic
1. - A package is **bulky** if its volume (Width x Height x Length) is greater than or equal to 1,000,000 cm³ or when one of its dimensions is greater or equal to 150 cm.
- A package is **heavy** when its mass is greater or equal to 20 kg.
2. The function returns the following strings based on the package properties.

- **STANDARD**: standard packages (those that are not bulky or heavy) can be handled normally.
- **SPECIAL**: packages that are either heavy or bulky can't be handled automatically.
- **REJECTED**: packages that are **both** heavy and bulky are rejected.
