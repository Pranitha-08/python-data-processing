from typing import Iterator


def read_in_chunks(file_path: str, chunk_size: int = 1000) -> Iterator[str]:
    """
    Read a text file line by line in chunks.
    """
    with open(file_path, "r", encoding="utf-8") as file:
        chunk = []

        for line in file:
            chunk.append(line.strip())

            if len(chunk) == chunk_size:
                yield chunk
                chunk = []

        if chunk:
            yield chunk
