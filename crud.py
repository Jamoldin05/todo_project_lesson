import logging

tasks = []

def create_task(title):
    tasks.append({"title": title, "done": False})
    logging.info(f"Yangi task qo‘shildi: {title}")

def get_all_tasks():
    logging.info(f"{len(tasks)} ta task qaytarildi")
    return tasks

def update_task(index, new_title):
    if 0 <= index < len(tasks):
        old_title = tasks[index]["title"]
        tasks[index]["title"] = new_title
        logging.info(f"Task yangilandi: '{old_title}' → '{new_title}'")
    else:
        logging.warning(f"Yangilash xatosi: index {index} mavjud emas")

def delete_task(index):
    if 0 <= index < len(tasks):
        removed = tasks.pop(index)
        logging.info(f"Task o‘chirildi: {removed['title']}")
    else:
        logging.warning(f"O‘chirish xatosi: index {index} mavjud emas")
