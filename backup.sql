--
-- PostgreSQL database dump
--

\restrict vTBglp699b6NtzXacHaHr6b8o0ZzM51gZYGMJ5rgnicm3wFxSAQ55nQoYLRTre8

-- Dumped from database version 16.14
-- Dumped by pg_dump version 16.14

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- Name: click_events; Type: TABLE; Schema: public; Owner: linktracker
--

CREATE TABLE public.click_events (
    id integer NOT NULL,
    code character varying(10) NOT NULL,
    long_url character varying(2048) NOT NULL,
    clicked_at character varying(32) NOT NULL
);


ALTER TABLE public.click_events OWNER TO linktracker;

--
-- Name: click_events_id_seq; Type: SEQUENCE; Schema: public; Owner: linktracker
--

CREATE SEQUENCE public.click_events_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.click_events_id_seq OWNER TO linktracker;

--
-- Name: click_events_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: linktracker
--

ALTER SEQUENCE public.click_events_id_seq OWNED BY public.click_events.id;


--
-- Name: shortened_urls; Type: TABLE; Schema: public; Owner: linktracker
--

CREATE TABLE public.shortened_urls (
    id integer NOT NULL,
    code character varying(10) NOT NULL,
    long_url character varying(2048) NOT NULL,
    created_at timestamp without time zone,
    hit_count integer
);


ALTER TABLE public.shortened_urls OWNER TO linktracker;

--
-- Name: shortened_urls_id_seq; Type: SEQUENCE; Schema: public; Owner: linktracker
--

CREATE SEQUENCE public.shortened_urls_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.shortened_urls_id_seq OWNER TO linktracker;

--
-- Name: shortened_urls_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: linktracker
--

ALTER SEQUENCE public.shortened_urls_id_seq OWNED BY public.shortened_urls.id;


--
-- Name: click_events id; Type: DEFAULT; Schema: public; Owner: linktracker
--

ALTER TABLE ONLY public.click_events ALTER COLUMN id SET DEFAULT nextval('public.click_events_id_seq'::regclass);


--
-- Name: shortened_urls id; Type: DEFAULT; Schema: public; Owner: linktracker
--

ALTER TABLE ONLY public.shortened_urls ALTER COLUMN id SET DEFAULT nextval('public.shortened_urls_id_seq'::regclass);


--
-- Data for Name: click_events; Type: TABLE DATA; Schema: public; Owner: linktracker
--

COPY public.click_events (id, code, long_url, clicked_at) FROM stdin;
1	WkrHgB	https://github.com/shivkumarkonnuri/linktracker	2026-06-14T13:13:21.948264+00:00
2	DgbhAx	https://github.com/shivkumarkonnuri/linktracker	2026-06-14T13:13:32.958155+00:00
3	DgbhAx	https://github.com/shivkumarkonnuri/linktracker	2026-06-14T13:15:38.166002+00:00
4	DgbhAx	https://github.com/shivkumarkonnuri/linktracker	2026-06-14T13:15:54.750036+00:00
\.


--
-- Data for Name: shortened_urls; Type: TABLE DATA; Schema: public; Owner: linktracker
--

COPY public.shortened_urls (id, code, long_url, created_at, hit_count) FROM stdin;
1	2wCRDf	https://kubernetes.io/docs/home/	2026-06-14 12:06:59.821392	0
2	wNcY2p	https://kubernetes.io/docs/home/	2026-06-14 12:30:16.194906	0
3	zJ4yl7	https://kubernetes.io/docs/home/	2026-06-14 12:34:07.398962	0
4	di20qc	https://github.com/shivkumarkonnuri/linktracker	2026-06-14 12:48:53.929248	0
5	XxczyS	https://github.com/shivkumarkonnuri/linktracker	2026-06-14 13:01:05.837832	0
6	DO9QsM	https://github.com/shivkumarkonnuri/linktracker	2026-06-14 13:01:06.805238	0
7	LmN3cS	https://github.com/shivkumarkonnuri/linktracker	2026-06-14 13:01:35.618025	0
8	pKQdnx	https://kubernetes.io/docs/home/	2026-06-14 13:02:00.977318	0
9	WkrHgB	https://github.com/shivkumarkonnuri/linktracker	2026-06-14 13:13:20.12669	1
10	DgbhAx	https://github.com/shivkumarkonnuri/linktracker	2026-06-14 13:13:29.945188	3
11	tp8Z7o	https://github.com/shivkumarkonnuri/linktracker	2026-06-14 15:27:38.751178	0
\.


--
-- Name: click_events_id_seq; Type: SEQUENCE SET; Schema: public; Owner: linktracker
--

SELECT pg_catalog.setval('public.click_events_id_seq', 4, true);


--
-- Name: shortened_urls_id_seq; Type: SEQUENCE SET; Schema: public; Owner: linktracker
--

SELECT pg_catalog.setval('public.shortened_urls_id_seq', 11, true);


--
-- Name: click_events click_events_pkey; Type: CONSTRAINT; Schema: public; Owner: linktracker
--

ALTER TABLE ONLY public.click_events
    ADD CONSTRAINT click_events_pkey PRIMARY KEY (id);


--
-- Name: shortened_urls shortened_urls_pkey; Type: CONSTRAINT; Schema: public; Owner: linktracker
--

ALTER TABLE ONLY public.shortened_urls
    ADD CONSTRAINT shortened_urls_pkey PRIMARY KEY (id);


--
-- Name: ix_click_events_code; Type: INDEX; Schema: public; Owner: linktracker
--

CREATE INDEX ix_click_events_code ON public.click_events USING btree (code);


--
-- Name: ix_shortened_urls_code; Type: INDEX; Schema: public; Owner: linktracker
--

CREATE UNIQUE INDEX ix_shortened_urls_code ON public.shortened_urls USING btree (code);


--
-- PostgreSQL database dump complete
--

\unrestrict vTBglp699b6NtzXacHaHr6b8o0ZzM51gZYGMJ5rgnicm3wFxSAQ55nQoYLRTre8

