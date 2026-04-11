UPDATE dishes
SET search_vector =
  to_tsvector('russian', coalesce(name,'') || ' ' || coalesce(description,''));

CREATE INDEX idx_fts_dishes
ON dishes USING GIN (search_vector);

CREATE FUNCTION dishes_search_vector_update() 
RETURNS trigger AS $$
BEGIN
  NEW.search_vector :=
    to_tsvector('russian',
      coalesce(NEW.name, '') || ' ' || coalesce(NEW.description, '')
    );
  RETURN NEW;
END
$$ LANGUAGE plpgsql;

CREATE TRIGGER dishes_tsvector_trigger
BEFORE INSERT OR UPDATE
ON dishes
FOR EACH ROW
EXECUTE FUNCTION dishes_search_vector_update();
