-- Table: public.Personel

-- DROP TABLE public."Personel";

SET default_tablespace = pg_default;

CREATE TABLE public."userTypes"(
    "id" serial not null,
    primary key(id),
	userrole character varying(20)
)

INSERT INTO public."userTypes"(userrole) VALUES ('admin');
INSERT INTO public."userTypes"(userrole) VALUES ('koordinator');
INSERT INTO public."userTypes"(userrole) VALUES ('nakliyeci');

select * from public."userTypes";

CREATE TABLE public."Personel"
(
    "personel_tipi" character varying(25),
    "tckn" character varying(11) COLLATE pg_catalog."default" NOT NULL,
    "soyad" character varying(50) COLLATE pg_catalog."default",
    "ad" character varying(50) COLLATE pg_catalog."default",
    "tel_no" character varying(20) COLLATE pg_catalog."default",
    "email" character varying(20) COLLATE pg_catalog."default",
    CONSTRAINT "personel_pkey" PRIMARY KEY ("tckn"),
    CONSTRAINT "personel_tckn_key" UNIQUE ("tckn")
)

 -- Table: public.Cekirdek

-- DROP TABLE public."Cekirdek";

CREATE TABLE public."Cekirdek"
(
    "koken" character varying(50) COLLATE pg_catalog."default",
    "miktar" integer,
    "tur" character varying(50) COLLATE pg_catalog."default" NOT NULL,
    "id" serial not null,
    primary key(id)
)

-- Table: public.Arac

-- DROP TABLE public."Arac";

CREATE TABLE public."Arac"
(
    "kapasite" integer,
    "plaka" character varying(20) COLLATE pg_catalog."default" NOT NULL,
    "sofor_tckn" character varying(20) COLLATE pg_catalog."default",
    CONSTRAINT "arac_pkey" PRIMARY KEY ("plaka")
)


-- Table: public.Paket_Kahve

-- DROP TABLE public."Paket_Kahve";

CREATE TABLE public."Paket_Kahve"
(
    "gramaj" integer,
    "skt" date,
    "tur" character varying(50) COLLATE pg_catalog."default",
    "id" serial not null,
    primary key(id)
)


CREATE INDEX "tur" ON public."Paket_Kahve"("tur");

-- Table: public.Uretici

-- DROP TABLE public."Uretici";

CREATE TABLE public."Uretici"
(
    "ad_soyad" character varying(100) COLLATE pg_catalog."default",
    "tckn" character varying(11) COLLATE pg_catalog."default" NOT NULL,
    "koy" character varying(50) COLLATE pg_catalog."default",
    "tel_no" character varying(20) COLLATE pg_catalog."default",
    CONSTRAINT "uretici_pkey" PRIMARY KEY ("tckn")
)



-- Table: public.Islem_Turu

CREATE TABLE public."Islem_Turu"
(
    "tur_id" integer NOT NULL,
    "islem_ismi" character varying(50),
    primary key ("tur_id")
)

-- Table: public.Satin_Alir

-- DROP TABLE public."Satin_Alir";

CREATE TABLE public."Satin_Alir"
(
    "odeme_tarihi" date,
    "odeme_miktari" integer,
    "aciklama" character varying(200) COLLATE pg_catalog."default",
    "uretici_tckn" character varying(20) COLLATE pg_catalog."default",
    "urun_miktari" integer,
    "plaka" character varying(20),
    "id" serial not null,
    primary key(id),
    CONSTRAINT "satin_alir_uretici_tckn_fkey" FOREIGN KEY ("uretici_tckn")
        REFERENCES public."Uretici" ("tckn") MATCH SIMPLE ON DELETE CASCADE
        ON update cascade
)

-- Index: uretici_tckn_fkey

-- DROP INDEX public.uretici_tckn_fkey;

CREATE INDEX uretici_tckn_fkey ON public."Satin_Alir" USING btree("uretici_tckn");

-- Table: public.Ogutme

-- DROP TABLE public."Ogutme";

CREATE TABLE public."Ogutme"
(
    "sorumlu_koordinator_tckn" character varying(11) COLLATE pg_catalog."default",
    "tur_id" integer,
    "giren_miktar" integer,
    "cikan_miktar" integer,
    "islem_suresi" integer,
    "bitti_mi" boolean,
    "id" serial not null,
    primary key(id),
    CONSTRAINT "ogutme_tur_id_fkey" FOREIGN KEY ("tur_id")
        REFERENCES public."Islem_Turu" ("tur_id") MATCH SIMPLE ON DELETE CASCADE
        On update cascade,
    CONSTRAINT "islem_turu_sorumlu_koordinator_tckn_fkey" FOREIGN KEY ("sorumlu_koordinator_tckn")
        REFERENCES public."Personel"("tckn") MATCH SIMPLE ON DELETE CASCADE
        ON update cascade
)

-- Index: islem_turu_fkey

-- DROP INDEX public.islem_turu_fkey;

CREATE INDEX islem_turu_fkey ON public."Ogutme" USING btree("tur_id");

-- Index: sorumlu_koordinator_tckn_fkey

-- DROP INDEX public.sorumlu_koordinator_tckn_fkey;

CREATE INDEX sorumlu_koordinator_tckn_fkey ON public."Ogutme"("sorumlu_koordinator_tckn")


-- Table: public.Kavurma

-- DROP TABLE public."Kavurma";

CREATE TABLE public."Kavurma"
(
    "sorumlu_koordinator_tckn" character varying(20) COLLATE pg_catalog."default",
    "tur_id" integer,
    "giren_miktar" integer,
    "cikan_miktar" integer,
    "islem_suresi" integer,
    bitti_mi boolean,
    "id" serial not null,
    primary key(id),
    CONSTRAINT "kavurma_tur_id_fkey" FOREIGN KEY ("tur_id")
        REFERENCES public."Islem_Turu" ("tur_id") MATCH SIMPLE ON DELETE CASCADE
        On update cascade,
    CONSTRAINT "islem_turu_sorumlu_koordinator_tckn_fkey" FOREIGN KEY ("sorumlu_koordinator_tckn")
        REFERENCES public."Personel" ("tckn") MATCH SIMPLE ON DELETE CASCADE
        ON update cascade
)


CREATE INDEX sorumlu_koordinator_tckn_fkey2 ON public."Kavurma"("sorumlu_koordinator_tckn")

CREATE INDEX turid_fkey ON public."Kavurma" USING btree("tur_id");



-- Table: public.IslemSonu

-- DROP TABLE public."Islem_Sonu";

CREATE TABLE public."Islem_Sonu"(
    "sorumlu_koordinator_tckn" character varying(20) COLLATE pg_catalog."default",
    "tur_id" integer,
    "id" serial not null,
    primary key(id),
    "id2" integer,
    "id3" integer,
    CONSTRAINT "id2_fkey" FOREIGN KEY ("id2")
        REFERENCES public."Ogutme" ("id") MATCH SIMPLE ON DELETE CASCADE
        On update cascade,
    CONSTRAINT "id23_fkey" FOREIGN KEY ("id3")
        REFERENCES public."Kavurma" ("id") MATCH SIMPLE ON DELETE CASCADE
        On update cascade,
     CONSTRAINT "son_tur_id_fkey" FOREIGN KEY ("tur_id")
        REFERENCES public."Islem_Turu" ("tur_id") MATCH SIMPLE ON DELETE CASCADE
        On update cascade,
    CONSTRAINT "islem_turu_sorumlu_koordinator_tckn_fkey" FOREIGN KEY ("sorumlu_koordinator_tckn")
        REFERENCES public."Personel" ("tckn") MATCH SIMPLE ON DELETE CASCADE
        ON update cascade
)


CREATE INDEX sorumlu_koordinator_tckn_fkey3 ON public."Islem_Sonu"("sorumlu_koordinator_tckn")


CREATE INDEX tur_id_islemsonu2 ON public."Islem_Sonu"("tur_id")

CREATE INDEX id_seri ON public."Islem_Sonu"(id2)

CREATE INDEX id_seri_2 ON public."Islem_Sonu"(id3)

-- Table: public.Alici

-- DROP TABLE public."Alici";

CREATE TABLE public."Alici"
(
    "sirket_adi" character varying(50) COLLATE pg_catalog."default",
    "sirket_id" character varying(50) COLLATE pg_catalog."default" NOT NULL,
    CONSTRAINT "Alici_pkey" PRIMARY KEY ("sirket_id")
)


-- Table: public.Satis

-- DROP TABLE public."Satis";

CREATE TABLE public."Satis"(
    "ucret" integer,
    "tarih" date,
    "miktar" integer,
    "alici_sirket_id" character varying(50) COLLATE pg_catalog."default",
    "id" serial not null,
    primary key(id),
    CONSTRAINT "satis_alici_sirket_id_fkey" FOREIGN KEY ("alici_sirket_id")
        REFERENCES public."Alici" ("sirket_id") MATCH SIMPLE ON DELETE CASCADE
        ON update cascade
)

-- Index: sirket_id_fk

-- DROP INDEX public.sirket_id_fk;

CREATE INDEX sirket_id_fk ON public."Satis" USING btree("alici_sirket_id");

CREATE TABLE public."Login"(
    "tckn" character varying(11) COLLATE pg_catalog."default" NOT NULL,
    "passcode" character varying(25),
    "personel_tipi" character varying(25),
    unique("passcode"),
    primary key(tckn)
)


CREATE INDEX tckn_fkey ON public."Personel" USING btree("tckn");


CREATE TABLE public."Iletisim"
(
    "email" character varying(50) COLLATE pg_catalog."default",
    "mesaj" character varying(999) COLLATE pg_catalog."default" NOT NULL,
    "id" serial not null,
    primary key(id)
)

INSERT INTO public."Personel" VALUES ('admin', '4', 'admin', 'admin', '999', 'admin@mail.com')
INSERT INTO public."Personel" VALUES ('koordinator', '2', 'koordinator', 'koordinator', '888', 'koordinator@mail.com')
INSERT INTO public."Personel" VALUES ('nakliyeci', '3', 'nakliyeci', 'nakliyeci', '999', 'nakliyeci@mail.com')

INSERT INTO public."Login" VALUES ('1', 'admin', 'admin')
INSERT INTO public."Login" VALUES ('2', 'koordinator', 'koordinator')
INSERT INTO public."Login" VALUES ('3', 'nakliyeci', 'nakliyeci')

INSERT INTO public."Islem_Turu" VALUES ('1', 'Öğütme')
INSERT INTO public."Islem_Turu" VALUES ('2', 'Kavurma')