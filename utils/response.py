def success_response(data):
    return {
        "success": True,
        "count": len(data),
        "data": data
    }