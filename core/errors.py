import time
import logging

def handle_api_error(logger, error_code, error_message):    
    if error_code in [452, 453, 454]:
        logger.critical(f"Authentication issue detected! {error_message}. Check your token.")
    
    elif error_code == 429:
        logger.warning("Rate limit hit.")
    
    elif error_code == 497:
        logger.info("Inventory full.")
        return None 

    elif error_code in [498, 499]:
        logger.error(f"Character issue: {error_message}. May need manual intervention.")
    
    elif error_code in [471, 478]:
        logger.warning(f"Item issue: {error_message}. Check your inventory.")
    
    elif error_code in [460, 461, 462]:
        logger.error(f"Banking error: {error_message}. Transaction failed.")
    
    elif error_code in [500, 597, 598]:
        logger.critical("API Server issue detected.")

    else:
        logger.error(f"Unhandled error {error_code}: {error_message}")

    return None