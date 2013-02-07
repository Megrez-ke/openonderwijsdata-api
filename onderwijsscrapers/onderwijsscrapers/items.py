from scrapy.item import Item, Field


class SchoolItem(Item):
    name = Field()  # `naam`
    brin = Field()  # `BRIN-nummer`
    branch_id = Field()  # Vestigingsnummer
    address = Field()  # `adres`
    zip_code = Field()  # `postcode`
    city = Field()  # `woonplaats`
    website = Field()  # `website` or `homepage`
    denomination = Field()  # `denominatie`
    education_structures = Field()  # `Onderwijsaanbod`


class SchoolVOItem(SchoolItem):
    # Holds the indicators that are available for this school
    available_indicators = Field()

    board_id = Field()  # Bevoegd gezagnummer
    schoolvo_id = Field()  # `school_id`
    schoolvo_code = Field()  # `school_code`
    municipality = Field()  # `gemeente`
    municipality_code = Field()  # `gemeente_code`
    province = Field()  # `provincie`
    longitude = Field()  # `longitude`
    latitude = Field()  # `latitude`
    phone = Field()  # `telefoon`
    email = Field()  # `e_mail`
    board = Field()  # `Bestuur` or `Bevoegd gezag`
    schoolvo_status_id = Field()  # `venster_status_id`
    schoolkompas_status_id = Field()  # `schoolkompas_status_id`
    logo_img_url = Field()  # `pad_logo`
    building_img_url = Field()  # `pad_gebouw`
    profile = Field()  # `Profiel`
    graduations = Field()  # `Slaagpercentage`
    student_satisfaction = Field()  # `Tevredenheid leerlingen`
    parent_satisfaction = Field()  # `Tevredenheid ouders`
    costs = Field()  # `Schoolkosten`


class OnderwijsInspectieItem(SchoolItem):
    rating = Field()
    rating_date = Field()
    rating_excerpt = Field()
    rating_history = Field()
    reports = Field()
    education_sector = Field()


class VOSchool(OnderwijsInspectieItem):
    board = Field()  # `Bestuur` or `Bevoegd gezag`
    board_id = Field()  # Bevoegd gezagnummer
    result_card_url = Field()  # Opbrengstenkaart URL

    # Field used to merge all sectors of a single school into one item.
    # This field is not stored.
    education_structures_to_scrape = Field()


class POSchool(OnderwijsInspectieItem):
    pass


class DUOSchoolItem(SchoolItem):
    publication_year = Field()  # year in which the file was published by DUO
    province = Field()  # `provincie`
    board_id = Field()  # Bevoegd gezagnummer
    municipality = Field()  # `Gemeente naam`
    municipality_code = Field()  # `Gemeente nummer`
    phone = Field()  # `telefoonnummer`
    correspondence_address = Field()  # `Straatnaam correspondentieadres`
    correspondence_zip = Field()  # `POSTCODE CORRESPONDENTIEADRES`
    correspondence_city = Field()  # `PLAATSNAAM CORRESPONDENTIEADRES`
    nodal_area = Field()  # `NODAAL GEBIED NAAM`
    nodal_area_code = Field()  # `NODAAL GEBIED CODE`
    rpa_area = Field()  # `RPA GEBIED NAAM`
    rpa_area_code = Field()  # `RPA GEBIED CODE`
    wgr_area = Field()  # `WGR GEBIED NAAM`
    wgr_area_code = Field()  # `WGR GEBIED CODE`
    corop_area = Field()  # `COROP GEBIED NAAM`
    corop_area_code = Field()  # `COROP GEBIED CODE`
    education_area = Field()  # `ONDERWIJS GEBIED NAAM`
    education_area_code = Field()  # `ONDERWIJS GEBIED CODE`
    rmc_region = Field()  # `RMC REGIO NAAM`
    rmc_region_code = Field()  # `RMC REGIO CODE`

    # Contents of "02. Leerlingen per vestiging naar postcode leerling
    # en leerjaar"
    student_residences = Field()

    # Contents of "01. Leerlingen per vestiging naar onderwijstype, lwoo
    # indicatie, sector, afdeling, opleiding"
    students_by_structure = Field()

    # Content of "06. Examenkandidaten en geslaagden"
    graduations = Field()
