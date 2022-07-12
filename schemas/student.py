from typing import Dict, List


def student_entity(db_item) -> Dict:
    return {
        "id": str(db_item["_id"]),
        "name": db_item["name"],
        "email": db_item["email"]
    }


def list_student_entity(db_item_list) -> List[Dict]:
    student_entities = []
    for db_item in db_item_list:
        student_entities.append(student_entity(db_item))

    return student_entities
