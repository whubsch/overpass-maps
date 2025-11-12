# Overpass Maps

This repository is designed to highlight maps that I think are cool and will hopefully spark inspiration for other OpenStreetMap mappers. Each directory contains a different map visualization showcasing unique aspects of OpenStreetMap data.

## Structure

Each directory in the `data/` folder represents a different map theme and contains two key files:

- **`.yaml`** - The style configuration that defines how the map looks (icons, colors, layout, etc.)
- **`.txt`** - The Overpass query that fetches the specific OSM data for this map

The GitHub workflow automatically combines these files into a format that can be used by Overpass Ultra.

## Tools

These maps are powered by [Overpass Ultra](https://overpass-ultra.us/), an amazing tool for querying and visualizing OpenStreetMap data. If you haven't checked it out yet, you absolutely should!

## Development

To regenerate the `.ultra` files from the source YAML and TXT files, run:

```bash
python3 scripts/concatenate_files.py
```

The GitHub Actions workflow will verify that generated files are up to date on every push and pull request.

## Contributing

Have an idea for a cool map? Feel free to open a PR with a new directory in the `data/` folder containing your style and query files! Don't forget to run the concatenation script to generate the `.ultra` file.

## License

Maps and queries in this repository are available the MIT License. See the [LICENSE](LICENSE.md) file for more details.
