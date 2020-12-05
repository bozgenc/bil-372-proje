-- Table: public.Personel

-- DROP TABLE public."Personel";

CREATE TABLE public."Personel"
(
    "Tur" integer,
    "TCKN" character varying(20) COLLATE pg_catalog."default" NOT NULL,
    "Soyad" character varying(50) COLLATE pg_catalog."default",
    "Nakliyeci_TCKN" character varying(20) COLLATE pg_catalog."default" NOT NULL,
    "Koordinator_TCKN" character varying(20) COLLATE pg_catalog."default" NOT NULL,
    "Ad" character varying(50) COLLATE pg_catalog."default",
    "Tel_No" character varying(20) COLLATE pg_catalog."default",
    CONSTRAINT "Personel_pkey" PRIMARY KEY ("TCKN", "Nakliyeci_TCKN", "Koordinator_TCKN"),
    CONSTRAINT "Personel_TCKN_key" UNIQUE ("TCKN")
)

TABLESPACE pg_default;

ALTER TABLE public."Personel"
    OWNER to postgres;
    
    
    
    
    
    
 -- Table: public.Cekirdek

-- DROP TABLE public."Cekirdek";

CREATE TABLE public."Cekirdek"
(
    "Koken" character varying(50) COLLATE pg_catalog."default",
    "Miktar" integer,
    "Tur" character varying(50) COLLATE pg_catalog."default" NOT NULL,
    CONSTRAINT "Cekirdek_pkey" PRIMARY KEY ("Tur")
)

TABLESPACE pg_default;

ALTER TABLE public."Cekirdek"
    OWNER to postgres;
    
    
    
    
    
  
  
  
-- Table: public.Arac

-- DROP TABLE public."Arac";

CREATE TABLE public."Arac"
(
    "Kapasite" integer,
    "Plaka" character varying(20) COLLATE pg_catalog."default" NOT NULL,
    "Sofor_TCKN" character varying(20) COLLATE pg_catalog."default",
    CONSTRAINT "Arac_pkey" PRIMARY KEY ("Plaka"),
    CONSTRAINT "Arac_Sofor_TCKN_fkey" FOREIGN KEY ("Sofor_TCKN")
        REFERENCES public."Personel" ("TCKN") MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION
        NOT VALID
)

TABLESPACE pg_default;

ALTER TABLE public."Arac"
    OWNER to postgres;
-- Index: sofor_tckn_fkey

-- DROP INDEX public.sofor_tckn_fkey;

CREATE INDEX sofor_tckn_fkey
    ON public."Arac" USING btree
    ("Sofor_TCKN" COLLATE pg_catalog."default" ASC NULLS LAST)
    TABLESPACE pg_default;
  
  
  
  
  
  
  



-- Table: public.Paket_Kahve

-- DROP TABLE public."Paket_Kahve";

CREATE TABLE public."Paket_Kahve"
(
    "Gramaj" integer,
    "SKT" date,
    "Tur" character varying(50) COLLATE pg_catalog."default",
    CONSTRAINT "Paket_Kahve_Tur_fkey" FOREIGN KEY ("Tur")
        REFERENCES public."Cekirdek" ("Tur") MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION
)

TABLESPACE pg_default;

ALTER TABLE public."Paket_Kahve"
    OWNER to postgres;
-- Index: Tur

-- DROP INDEX public."Tur";

CREATE INDEX "Tur"
    ON public."Paket_Kahve" USING btree
    ("Tur" COLLATE pg_catalog."default" ASC NULLS LAST)
    TABLESPACE pg_default;
    
    
    
    
    
    
    
    
    
    
    
    
-- Table: public.Uretici

-- DROP TABLE public."Uretici";

CREATE TABLE public."Uretici"
(
    "Ad" character varying(50) COLLATE pg_catalog."default",
    "Soyad" character varying(50) COLLATE pg_catalog."default",
    "TCKN" character varying(20) COLLATE pg_catalog."default" NOT NULL,
    "Koy" character varying(50) COLLATE pg_catalog."default",
    "Tel_No" character varying(20) COLLATE pg_catalog."default",
    CONSTRAINT "Uretici_pkey" PRIMARY KEY ("TCKN")
)

TABLESPACE pg_default;

ALTER TABLE public."Uretici"
    OWNER to postgres;
    
    
    
    
    
    
    
    
-- Table: public.Islem_Turu

-- DROP TABLE public."Islem_Turu";

CREATE TABLE public."Islem_Turu"
(
    "Sorumlu_Koordinator_TCKN" character varying(20) COLLATE pg_catalog."default",
    "Tur_ID" integer NOT NULL,
    CONSTRAINT "Islem_Turu_pkey" PRIMARY KEY ("Tur_ID"),
    CONSTRAINT "Islem_Turu_Sorumlu_Koordinator_TCKN_fkey" FOREIGN KEY ("Sorumlu_Koordinator_TCKN")
        REFERENCES public."Personel" ("TCKN") MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION
)

TABLESPACE pg_default;

ALTER TABLE public."Islem_Turu"
    OWNER to postgres;
-- Index: sorumlu_koordinator_tckn_fkey

-- DROP INDEX public.sorumlu_koordinator_tckn_fkey;

CREATE INDEX sorumlu_koordinator_tckn_fkey
    ON public."Islem_Turu" USING btree
    ("Sorumlu_Koordinator_TCKN" COLLATE pg_catalog."default" ASC NULLS LAST)
    TABLESPACE pg_default;
    
    
    
    
    
    
    
    
    
    
    
    
    
-- Table: public.Satin_Alir

-- DROP TABLE public."Satin_Alir";

CREATE TABLE public."Satin_Alir"
(
    "Odeme_Tarihi" date,
    "Odeme_Miktari" integer,
    "Aciklama" character varying(200) COLLATE pg_catalog."default",
    "Uretici_TCKN" character varying(20) COLLATE pg_catalog."default",
    "Urun_Miktari" integer,
    CONSTRAINT "Satin_Alir_Uretici_TCKN_fkey" FOREIGN KEY ("Uretici_TCKN")
        REFERENCES public."Uretici" ("TCKN") MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION
)

TABLESPACE pg_default;

ALTER TABLE public."Satin_Alir"
    OWNER to postgres;
-- Index: uretici_tckn_fkey

-- DROP INDEX public.uretici_tckn_fkey;

CREATE INDEX uretici_tckn_fkey
    ON public."Satin_Alir" USING btree
    ("Uretici_TCKN" COLLATE pg_catalog."default" ASC NULLS LAST)
    TABLESPACE pg_default;
    
    
    
    
    
    
-- Table: public.Ogutme

-- DROP TABLE public."Ogutme";

CREATE TABLE public."Ogutme"
(
    "Tur_ID" integer,
    "Giren_Miktar" integer,
    "Cikan_Miktar" integer,
    "Islem_Suresi" integer,
    CONSTRAINT "Ogutme_Tur_ID_fkey" FOREIGN KEY ("Tur_ID")
        REFERENCES public."Islem_Turu" ("Tur_ID") MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION
)

TABLESPACE pg_default;

ALTER TABLE public."Ogutme"
    OWNER to postgres;
-- Index: islem_turu_fkey

-- DROP INDEX public.islem_turu_fkey;

CREATE INDEX islem_turu_fkey
    ON public."Ogutme" USING btree
    ("Tur_ID" ASC NULLS LAST)
    TABLESPACE pg_default;
    
    




-- Table: public.Kavurma

-- DROP TABLE public."Kavurma";

CREATE TABLE public."Kavurma"
(
    "Tur_ID" integer,
    "Giren_Miktar" integer,
    "Cikan_Miktar" integer,
    "Islem_Suresi" integer,
    CONSTRAINT "Kavurma_Tur_ID_fkey" FOREIGN KEY ("Tur_ID")
        REFERENCES public."Islem_Turu" ("Tur_ID") MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION
)

TABLESPACE pg_default;

ALTER TABLE public."Kavurma"
    OWNER to postgres;
-- Index: turid_fkey

-- DROP INDEX public.turid_fkey;

CREATE INDEX turid_fkey
    ON public."Kavurma" USING btree
    ("Tur_ID" ASC NULLS LAST)
    TABLESPACE pg_default;
    
    
    
    
-- Table: public.Alici

-- DROP TABLE public."Alici";

CREATE TABLE public."Alici"
(
    "Sirket_Adi" character varying(50) COLLATE pg_catalog."default",
    "Sirket_ID" character varying(50) COLLATE pg_catalog."default" NOT NULL,
    CONSTRAINT "Alici_pkey" PRIMARY KEY ("Sirket_ID")
)

TABLESPACE pg_default;

ALTER TABLE public."Alici"
    OWNER to postgres;
    
    
    
    
    
    
    
    
-- Table: public.Satis

-- DROP TABLE public."Satis";

CREATE TABLE public."Satis"
(
    "Ucret" integer,
    "Tarih" date,
    "Miktar" integer,
    "Alici_Sirket_ID" character varying(50) COLLATE pg_catalog."default",
    CONSTRAINT "Satis_Alici_Sirket_ID_fkey" FOREIGN KEY ("Alici_Sirket_ID")
        REFERENCES public."Alici" ("Sirket_ID") MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION
)

TABLESPACE pg_default;

ALTER TABLE public."Satis"
    OWNER to postgres;
-- Index: sirket_id_fk

-- DROP INDEX public.sirket_id_fk;

CREATE INDEX sirket_id_fk
    ON public."Satis" USING btree
    ("Alici_Sirket_ID" COLLATE pg_catalog."default" ASC NULLS LAST)
    TABLESPACE pg_default;    
    
    
    
    
    
    
    

  
  
  
  
  
  
  
  