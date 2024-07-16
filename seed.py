from faker import Faker
from random import choice as rc, sample
from app import app, db
from models import User, Illness, Herbs, user_illness

# Create an instance of the Faker class
fake = Faker()

# Create lists to hold the data
users = []
illnesses = []
herbs = []

with app.app_context():
    db.create_all()

    # Delete all rows in tables
    User.query.delete()
    Illness.query.delete()
    Herbs.query.delete()
    db.session.commit()

    # Add model instances to database
    Isamar  = User(
        name="Isamar Gonzalez",
        username="isamar_g",
        email="isamar@example.com",
        password="password123"
    )
    Bobby  = User(
        name="Bobby Bans Jr",
        username="bobby_g",
        email="bobby@example.com",
        password="password123"
    )
    Jaylynn = User(
        name="Jaylynn Aaliyah Lula Banos",
        username="jaylynn_g",
        email="jaylynn@example.com",
        password="Rse309j"
    )
    db.session.add_all([Isamar, Bobby, Jaylynn])
    db.session.commit()

    # Create predefined illnesses
    Chronic_Illness = Illness(
        name="Chronic Illness",
        description="Bobby has a chronic illness that causes him to lose his appetite.",
        body_part="Pancreas",
        symptoms="Bobby's appetite is reduced, he is unable to eat, and his diet is poor.",
        treatment="Medication and diet management."
    )
    Panic_Disorder = Illness(
        name="Panic Disorder",
        description="Isamar has a chronic illness that causes panic attacks.",
        body_part="Nervous System",
        symptoms="Isamar's heart rate increases, she feels dizzy, and experiences shortness of breath.",
        treatment="Therapy and medication."
    )
    Chronic_Stress = Illness(
        name="Stress",
        description="Bobby has high levels of stress due to his workload.",
        body_part="Nervous System",
        symptoms="Bobby feels tense, has trouble sleeping, and experiences headaches.",
        treatment="Relaxation techniques and exercise."
    )
    Diabetes_type2 = Illness(
        name="Diabetes",
        description="diabetes which affects her blood sugar levels.",
        body_part="Pancreas",
        symptoms="Increased thirst, frequent urination, and fatigue.",
        treatment="Insulin and dietary changes."
    )

    db.session.add_all([Chronic_Illness, Panic_Disorder, Chronic_Stress, Diabetes_type2])
    db.session.commit()

    # Create predefined herbs
    Lavender = Herbs(
        name="Lavender",
        description="Lavender is used to help with relaxation and sleep.",
        health_benefits="Reduces stress and improves sleep quality.",
        side_effects="May cause skin irritation in some individuals.",
    )
    Ginseng = Herbs(
        name="Ginseng",
        description="Ginseng is used to improve energy and reduce stress.",
        health_benefits="Boosts energy levels and reduces stress.",
        side_effects="May cause headaches and digestive issues.",
    )

    db.session.add_all([Lavender, Ginseng])
    db.session.commit()

    # Add predefined illnesses with corresponding herbs
    predefined_illnesses = [
        Illness(
            name="Diabetes",
            description="A chronic condition affecting blood sugar regulation due to insufficient insulin production or use.",
            body_part="Pancreas",
            symptoms="Increased thirst, frequent urination, extreme hunger, fatigue, blurred vision.",
            treatment="Turkey Tail Tea"
        ),
        Illness(
            name="Migraines and Headaches",
            description="Recurrent, severe headaches often accompanied by other symptoms like nausea and sensitivity to light.",
            body_part="Head",
            symptoms="Intense throbbing pain, nausea, sensitivity to light and sound, visual disturbances.",
            treatment="Watercress or Rosemary Tea"
        ),
        Illness(
            name="Stress",
            description="A physical or emotional response to external pressures or demands.",
            body_part="Nervous system",
            symptoms="Tension, irritability, fatigue, difficulty concentrating, sleep disturbances.",
            treatment="Lion's Mane, Lavender Tea, meditation, exercise"
        ),
        Illness(
            name="Epilepsy and Seizures",
            description="A neurological disorder marked by recurrent, unprovoked seizures.",
            body_part="Brain",
            symptoms="Convulsions, loss of consciousness, staring spells, confusion, sensory disturbances.",
            treatment="CBD Oil, Valerian Root, Lavender, Mugwort, ketogenic diet"
        ),
        Illness(
            name="Panic Attacks",
            description="Sudden episodes of intense fear or anxiety, often with physical symptoms.",
            body_part="Nervous system",
            symptoms="Rapid heartbeat, sweating, shaking, shortness of breath, feelings of doom.",
            treatment="Reishi, Pulsatilla, Valerian Root, Chamomile Tea, breathing exercises, cognitive-behavioral therapy"
        ),
        Illness(
            name="Depression",
            description="A common and serious medical illness that negatively affects how you feel, the way you think, and how you act.",
            body_part="Brain",
            symptoms="Persistent sadness, loss of interest in activities, changes in appetite, trouble sleeping or sleeping too much, loss of energy, feelings of worthlessness or guilt, difficulty thinking, thoughts of death or suicide.",
            treatment="Ashwagandha, Evening Primrose, Lion's Mane, Motherwort, Valerian Root, St. John's Wort, Sugar Maple, Wild Rose"
        )
    ]

    db.session.add_all(predefined_illnesses)
    db.session.commit()

    predefined_herbs = [
        Herbs(
            name="Ashwagandha",
            description="Ashwagandha is an adaptogenic herb used in traditional Indian medicine to treat a variety of conditions, including stress, anxiety, and insomnia.",
            health_benefits="Ashwagandha helps reduce stress, anxiety, and improve sleep quality.",
            side_effects="Possible side effects include headaches, nausea, and stomach upset."
        ),
        Herbs(
            name="Evening Primrose",
            description="Evening Primrose is a plant whose oil is used to treat conditions like eczema, rheumatoid arthritis, and premenstrual syndrome (PMS).",
            health_benefits="Evening Primrose oil is known for its anti-inflammatory properties and benefits for skin health.",
            side_effects="May cause headaches, nausea, and upset stomach."
        ),
        Herbs(
            name="Lion's Mane",
            description="Lion's Mane is a mushroom used in traditional Chinese medicine to support brain health and cognitive function.",
            health_benefits="Lion's Mane helps improve cognitive function, reduce symptoms of anxiety and depression, and support nervous system health.",
            side_effects="Generally well-tolerated, but may cause mild digestive discomfort."
        ),
        Herbs(
            name="Motherwort",
            description="Motherwort is an herb used in traditional medicine to support heart health and reduce anxiety.",
            health_benefits="Motherwort is known for its calming effects and benefits for heart health.",
            side_effects="May cause digestive issues and skin reactions in some individuals."
        ),
        Herbs(
            name="Valerian Root",
            description="Valerian Root is an herb commonly used to treat insomnia and anxiety.",
            health_benefits="Valerian Root promotes relaxation and improves sleep quality.",
            side_effects="Possible side effects include headaches, dizziness, and stomach upset."
        ),
        Herbs(
            name="St. John's Wort",
            description="St. John's Wort is an herb used to treat depression and mood disorders.",
            health_benefits="St. John's Wort can help improve mood and alleviate symptoms of mild to moderate depression.",
            side_effects="Can interact with many medications; may cause photosensitivity, dry mouth, and dizziness."
        ),
        Herbs(
            name="Sugar Maple",
            description="Sugar Maple is known for its sap, which is used to make maple syrup, and it also has medicinal properties.",
            health_benefits="Maple sap and syrup contain antioxidants and can support immune health.",
            side_effects="Excessive consumption may lead to elevated blood sugar levels."
        ),
        Herbs(
            name="Wild Rose",
            description="Wild Rose, particularly its hips, are used for their high vitamin C content and antioxidant properties.",
            health_benefits="Wild Rose helps boost the immune system and support skin health.",
            side_effects="Generally safe, but may cause allergic reactions in some individuals.",
            illness_id=predefined_illnesses[-1].id  # Depression
        )
    ]
    herbs.extend(predefined_herbs)

    db.session.add_all(predefined_herbs)
    db.session.commit()

    # Generate fake users
    for _ in range(10):
        user = User(
            name=fake.name(),
            username=fake.user_name(),
            email=fake.email(),
            password=fake.password(),
        )
        users.append(user)

    db.session.add_all(users)
    db.session.commit()

    # # Generate fake illnesses and add to database
    # for _ in range(10):
    #     illness = Illness(
    #         name=fake.word(),
    #         description=fake.sentence(),
    #         body_part=fake.word(),
    #         symptoms=fake.sentence(),
    #         treatment=fake.sentence()
    #     )
    #     illnesses.append(illness)
        
    db.session.add_all(illnesses)
    db.session.commit()

    # Associate users with illnesses
    all_users = User.query.all()
    all_illnesses = Illness.query.all()

    for user in all_users:
        user.illnesses.extend(sample(all_illnesses, k=rc([1, 2, 3])))

    db.session.commit()

    # Associate illnesses with herbs
    all_herbs = Herbs.query.all()

    for illness in all_illnesses:
        illness.herbs.extend(sample(all_herbs, k=rc([1, 2, 3])))

    db.session.commit()

    print("Database seeded successfully!")
