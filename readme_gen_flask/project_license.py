from flask import jsonify, request


def project_license():
    # Optional: Retrieve license type or details from query parameters
    license_type = request.args.get("type", "MIT")  # Default to MIT if not provided

    # Generate license markdown based on the type
    if license_type == "MIT":
        license_markdown = """
# License

This project is licensed under the MIT License - see the [LICENSE](./LICENSE) file for details.
"""
    else:
        # Handle other types of licenses if needed
        license_markdown = f"""
# License

This project is licensed under the {license_type} License - see the [LICENSE](./LICENSE) file for details.
"""

    return jsonify({"license_markdown": license_markdown}), 200
