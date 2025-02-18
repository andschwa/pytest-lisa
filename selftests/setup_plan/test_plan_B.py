from __future__ import annotations

import functools
import typing

if typing.TYPE_CHECKING:
    from target import Target

import lisa

LISA = functools.partial(
    lisa.LISA, platform="Custom", category="Functional", area="self-test", priority=1
)


@LISA(features=["xdp"])
def test_xdp_b(target: Target) -> None:
    pass


@LISA(features=["gpu"])
def test_gpu_b(target: Target) -> None:
    pass


@LISA(features=["rdma"])
def test_rdma_b(target: Target) -> None:
    pass
