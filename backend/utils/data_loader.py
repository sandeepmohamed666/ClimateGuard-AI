import io
import pandas as pd
from pathlib import Path
from typing import Tuple, Union

def load_data(
    train_path: Union[str, Path],
    test_path: Union[str, Path],
    weather_path: Union[str, Path],
    nasa_path: Union[str, Path]
) -> Tuple[pd.DataFrame, pd.DataFrame, pd.DataFrame, pd.DataFrame]:
    """
    Loads train, test, weather, and NASA datasets.
    """

    train_df = pd.read_csv(train_path)
    test_df = pd.read_csv(test_path)
    weather_df = pd.read_csv(weather_path)

    # NASA POWER file includes a descriptive header before the CSV table.
    with open(nasa_path, "r", encoding="utf-8") as f:
        lines = f.readlines()

    header_idx = next(
        (i for i, line in enumerate(lines) if line.strip().startswith("YEAR,")),
        None,
    )
    if header_idx is None:
        raise ValueError(f"Unable to find CSV header in NASA file: {nasa_path}")

    nasa_df = pd.read_csv(
        io.StringIO("".join(lines[header_idx:])),
    )

    return train_df, test_df, weather_df, nasa_df