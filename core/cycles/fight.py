def fight(engine):
    engine.logger.info("Fighting")
    result = engine.safe_api_call(engine.api.fight, "Fight failed")
    if result is None:
        return
    engine.logger.info("Fight complete. Waiting for cooldown...")
    engine.cooldown(result)
    engine.logger.info("Resting")
    result = engine.safe_api_call(engine.api.rest, "Rest failed")
    if result is None:
        return
    engine.logger.info("Rest complete. Waiting for cooldown...")
    engine.cooldown(result)