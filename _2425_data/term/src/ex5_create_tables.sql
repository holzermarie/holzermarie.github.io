CREATE TABLE "Client" (
	"idC"	INTEGER,
	"nom"	TEXT,
	"prenom"	TEXT,
	"email"	TEXT,
	PRIMARY KEY("idC" AUTOINCREMENT)
);

CREATE TABLE "Location" (
	"idL"	INTEGER,
	"idCli"	INTEGER,
	"idVehi"	INTEGER,
	"dateDeb"	TEXT,
	"dateFin"	TEXT,
	FOREIGN KEY("idVehi") REFERENCES "Vehicule"("idV"),
	FOREIGN KEY("idCli") REFERENCES "Client"("idC"),
	PRIMARY KEY("idL" AUTOINCREMENT)
);

CREATE TABLE "Modele" (
	"idM"	INTEGER,
	"marque"	TEXT,
	"annee"	INTEGER,
	"moteur"	TEXT,
	PRIMARY KEY("idM" AUTOINCREMENT)
);

CREATE TABLE "Vehicule" (
	"idV"	INTEGER,
	"modele"	TEXT,
	"immatr"	TEXT,
	"nbKm"	INTEGER,
	FOREIGN KEY("modele") REFERENCES "Modele"("idM"),
	PRIMARY KEY("idV" AUTOINCREMENT)
);
