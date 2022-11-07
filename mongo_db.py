import pymongo


class MongoDB:
    def __init__(self):
        self.client = pymongo.MongoClient("mongodb+srv://admin:qwerty123456@cluster0.mpp95u0.mongodb.net/?retryWrites=true&w=majority")
        self.db = self.client.Data.posts

    def search_text(self, text):
        return list(self.db.find({"text": {"$regex": text}}).limit(20).sort("created_date", pymongo.DESCENDING))

    def delete_post(self, id: int):
        self.db.delete_one({"_id": id})
        return f"Post with id={id} has been deleted"

# if __name__ == "__main__":
