# Custom Tools Directory

Place your custom Python tools here. Each tool should be a module that exposes functions the AI model can use.

## Example Tool Structure

```python
# tools/material_calculator.py
def calculate_materials(length_ft, material_type):
    """
    Calculate materials needed for a project
    
    Args:
        length_ft: Length in feet
        material_type: Type of material (pipe, wire, etc.)
    
    Returns:
        dict with material quantities
    """
    # Your calculation logic
    return {"quantity": 100, "unit": "feet"}
```

The AI model will automatically discover these tools and know when to use them!

## Tools to Create

- Material calculator
- Labor estimator  
- Cost analyzer
- Schedule builder
- Document generator

