-- Table: public.Personel

-- DROP TABLE public."Personel";

SET default_tablespace = pg_default;

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
    CONSTRAINT "cekirdek_pkey" PRIMARY KEY ("tur")
)



-- Table: public.Arac

-- DROP TABLE public."Arac";

CREATE TABLE public."Arac"
(
    "kapasite" integer,
    "plaka" character varying(20) COLLATE pg_catalog."default" NOT NULL,
    "sofor_tckn" character varying(20) COLLATE pg_catalog."default",
    CONSTRAINT "arac_pkey" PRIMARY KEY ("plaka"),
    CONSTRAINT "arac_sofor_tckn_fkey" FOREIGN KEY ("sofor_tckn")
        REFERENCES public."Personel" ("tckn") MATCH SIMPLE
)

-- Index: sofor_tckn_fkey

-- DROP INDEX public.sofor_tckn_fkey;

CREATE INDEX sofor_tckn_fkey ON public."Arac"("sofor_tckn");




-- Table: public.Paket_Kahve

-- DROP TABLE public."Paket_Kahve";

CREATE TABLE public."Paket_Kahve"
(
    "gramaj" integer,
    "skt" date,
    "tur" character varying(50) COLLATE pg_catalog."default",
    "id" serial not null,
    primary key(id),
    CONSTRAINT "paket_kahve_tur_fkey" FOREIGN KEY ("tur")
        REFERENCES public."Cekirdek" ("tur") MATCH SIMPLE
)

-- Index: Tur

-- DROP INDEX public."Tur";

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

-- DROP TABLE public."Islem_Turu";

CREATE TABLE public."Islem_Turu"
(
    "sorumlu_koordinator_tckn" character varying(20) COLLATE pg_catalog."default",
    "tur_id" integer NOT NULL,
    CONSTRAINT "islem_turu_pkey" PRIMARY KEY ("tur_id"),
    CONSTRAINT "islem_turu_sorumlu_koordinator_tckn_fkey" FOREIGN KEY ("sorumlu_koordinator_tckn")
        REFERENCES public."Personel" ("tckn") MATCH SIMPLE
)

-- Index: sorumlu_koordinator_tckn_fkey

-- DROP INDEX public.sorumlu_koordinator_tckn_fkey;

CREATE INDEX sorumlu_koordinator_tckn_fkey ON public."Islem_Turu"("sorumlu_koordinator_tckn")

-- Table: public.Satin_Alir

-- DROP TABLE public."Satin_Alir";

CREATE TABLE public."Satin_Alir"
(
    "odeme_tarihi" date,
    "odeme_miktari" integer,
    "aciklama" character varying(200) COLLATE pg_catalog."default",
    "uretici_tckn" character varying(20) COLLATE pg_catalog."default",
    "urun_miktari" integer,
    "id" serial not null,
    primary key(id),
    CONSTRAINT "satin_alir_uretici_tckn_fkey" FOREIGN KEY ("uretici_tckn")
        REFERENCES public."Uretici" ("tckn") MATCH SIMPLE
)

-- Index: uretici_tckn_fkey

-- DROP INDEX public.uretici_tckn_fkey;

CREATE INDEX uretici_tckn_fkey ON public."Satin_Alir" USING btree("uretici_tckn");

-- Table: public.Ogutme

-- DROP TABLE public."Ogutme";

CREATE TABLE public."Ogutme"
(
    "tur_id" integer,
    "giren_miktar" integer,
    "cikan_miktar" integer,
    "islem_suresi" integer,
    bitti_mi integer,
    "id" serial not null,
    primary key(id),
    CONSTRAINT "ogutme_tur_id_fkey" FOREIGN KEY ("tur_id")
        REFERENCES public."Islem_Turu" ("tur_id") MATCH SIMPLE
)

-- Index: islem_turu_fkey

-- DROP INDEX public.islem_turu_fkey;

CREATE INDEX islem_turu_fkey ON public."Ogutme" USING btree("tur_id");


-- Table: public.Kavurma

-- DROP TABLE public."Kavurma";

CREATE TABLE public."Kavurma"
(
    "tur_id" integer,
    "giren_miktar" integer,
    "cikan_miktar" integer,
    "islem_suresi" integer,
    bitti_mi integer,
    "id" serial not null,
    primary key(id),
    CONSTRAINT "kavurma_tur_id_fkey" FOREIGN KEY ("tur_id")
        REFERENCES public."Islem_Turu" ("tur_id") MATCH SIMPLE
)
-- Table: public.IslemSonu

-- DROP TABLE public."Islem_Sonu";

CREATE TABLE public."Islem_Sonu"(
    "id" serial not null,
    primary key(id),
    "tur_id" integer,
    CONSTRAINT "islemsonu_tur_id_fkey" FOREIGN KEY ("tur_id")
        REFERENCES public."Islem_Turu" ("tur_id") MATCH SIMPLE
)
-- Index: turid_fkey

-- DROP INDEX public.turid_fkey;

CREATE INDEX turid_fkey2 ON public."Islem_Sonu" USING btree("tur_id");

-- Index: turid_fkey

-- DROP INDEX public.turid_fkey;

CREATE INDEX turid_fkey ON public."Kavurma" USING btree("tur_id");

-- Table: public.IslemSonu

-- DROP TABLE public."Islem_Sonu";

CREATE TABLE public."Islem_Sonu"(
    "id" serial not null,
    primary key(id),
    "tur_id" integer,
    CONSTRAINT "islemsonu_tur_id_fkey" FOREIGN KEY ("tur_id")
        REFERENCES public."Islem_Turu" ("tur_id") MATCH SIMPLE
)
-- Index: turid_fkey

-- DROP INDEX public.turid_fkey;

CREATE INDEX turid_fkey2 ON public."Islem_Sonu" USING btree("tur_id");
    
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

CREATE TABLE public."Satis"
(
    "ucret" integer,
    "tarih" date,
    "miktar" integer,
    "alici_sirket_id" character varying(50) COLLATE pg_catalog."default",
    "id" serial not null,
    primary key(id),
    CONSTRAINT "satis_alici_sirket_id_fkey" FOREIGN KEY ("alici_sirket_id")
        REFERENCES public."Alici" ("sirket_id") MATCH SIMPLE
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


CREATE INDEX tckn_fkey ON public."Personel" USING btree("tckn")













