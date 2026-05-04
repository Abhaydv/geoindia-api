import os
import pandas as pd

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from core.db import DATABASE_URL
from models.location import State, District, SubDistrict, Village

engine = create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine)
session = Session()

data_folder = r"C:\Users\abhay\OneDrive\Desktop\geoindia\data"


def read_any(file_path):
    for sep in [None, ",", ";", "\t", "|"]:
        try:
            df = pd.read_csv(file_path, encoding="latin1", sep=sep, engine="python")
            if len(df.columns) > 1:
                return df
        except:
            pass
    raise Exception("File parse failed")


for file in os.listdir(data_folder):
    file_path = os.path.join(data_folder, file)
    print(f"\n👉 Processing: {file}")

    try:
        df = read_any(file_path)
        df.columns = df.columns.str.strip()

        print("COLUMNS:", df.columns.tolist())
        print("TOTAL ROWS:", len(df))

    except Exception as e:
        print("❌ File error:", e)
        continue

    for i, row in df.iterrows():
        try:
            state_name = str(row.get("STATE NAME", "")).strip()
            district_name = str(row.get("DISTRICT NAME", "")).strip()
            sub_district_name = str(row.get("SUB-DISTRICT NAME", "")).strip()
            village_name = str(row.get("Area Name", "")).strip()

            # skip bad rows
            if village_name.lower() == "nan" or village_name == "":
                continue

            print(f"👉 INSERTING ROW {i}: {village_name}")

            # ---------- STATE ----------
            state = session.query(State).filter_by(name=state_name).first()
            if not state:
                state = State(name=state_name)
                session.add(state)
                session.commit()
                print("  ✔ STATE CREATED")

            # ---------- DISTRICT ----------
            district = session.query(District).filter_by(
                name=district_name, state_id=state.id
            ).first()

            if not district:
                district = District(name=district_name, state_id=state.id)
                session.add(district)
                session.commit()
                print("  ✔ DISTRICT CREATED")

            # ---------- SUB DISTRICT ----------
            sub = session.query(SubDistrict).filter_by(
                name=sub_district_name, district_id=district.id
            ).first()

            if not sub:
                sub = SubDistrict(name=sub_district_name, district_id=district.id)
                session.add(sub)
                session.commit()
                print("  ✔ SUBDISTRICT CREATED")

            # ---------- VILLAGE ----------
            village = Village(name=village_name, sub_district_id=sub.id)
            session.add(village)
            session.commit()   # 🔥 FORCE COMMIT

            print("  ✔ VILLAGE INSERTED")

        except Exception as e:
            print("❌ ERROR AT ROW:", i)
            print("DETAIL:", e)
            break   # stop on first error

session.close()
print("\n🔥 DONE")