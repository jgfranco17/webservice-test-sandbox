"""Initializes the v0 routes."""

from fastapi import APIRouter

from backend.routes.v0.handlers import simple_routes

router_v0 = APIRouter(prefix="/v0", tags=["V0"])
router_v0.include_router(simple_routes)
