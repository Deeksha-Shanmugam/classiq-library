from tests.utils_for_testbook import (
    validate_quantum_program_size,
    validate_quantum_model,
    wrap_testbook,
)
from testbook.client import TestbookNotebookClient


@wrap_testbook("rectangles_packing_grid", timeout_seconds=1800)
def test_notebook(tb: TestbookNotebookClient) -> None:
    pass  # TODO
