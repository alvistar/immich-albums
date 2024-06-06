# Immich Albums

## Overview
Immich Albums is a tool designed to create albums in Immich from a folder structure. 
Assets needs to be loaded as external library in Immich then you can launch script to create albums.

## Getting Started
### Prerequisites
- Immich instance running
- Python installed
- Poetry installed - https://python-poetry.org/docs/#installation

### Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/alvistar/immich-albums.git
   ```
2. Navigate to the project directory:
   ```bash
    cd immich-albums
    ```
3. Install dependencies:
4. ```bash
    poetry install
    ```
5. Activate virtual environment:
   ```bash
    poetry shell
    ```
6. Test installation:
   ```bash
    im --help
    ```
### Usage
You can get help of various args by running:
```bash
im --help
```
The following are required arguments:
- `--api-key` - Immich API key
- `--api-host` - Immich API host. Example: `https://localhost:22283/api`
- `--original-path` - Path to local albums
- `--replace-path` - Path as seen by Immich host

Original path is the path to your local albums. 
If for example your albums are stored in `/home/user/albums` and you mounted that path under docker as `/mnt/albums` 
you need to pass `/home/user/albums` as `--original-path` and `/mnt/albums` as `--replace-path`.

> [!NOTE]
> Api host should be the API endpoint of your Immich instance. 
>
> Example: `https://localhost:22283/api`

```bash
cd /home/user/albums
im --api-key YOUR_API_KEY --api-host YOUR_API_HOST --original-path /home/user/albums --replace-path /mnt/albums .
```

Instead of passing every argument you can create a config file in yaml format.
Default config file name is `config.yaml` and it should be placed in your home directory under *".config/immich-albums/config.yml"*

Example config file:
```yaml
api-key: YOUR_API_KEY
api-host: YOUR_API_HOST
original-path: /path/to/local/albums
replace-path: /path/as/seen/by/immich
```

Alternatively you can pass config file path as argument:
```bash
im --config /path/to/config/file
```

## Updating openapi client:

```bash
openapi-generator-cli generate -g python -o generated/openapi_client -i immich-openapi-specs.json -p packageVersion=1.105.1
poetry lock --no-update
```

## Contributing
Contributions to Immich Albums are welcome! 

## License
This project is licensed under the MIT license - see the [LICENSE.txt](LICENSE.txt) file for details.

## Acknowledgements
Big thanks to [Immich](https://github.com/immich-app/immich) for the incredible job!
