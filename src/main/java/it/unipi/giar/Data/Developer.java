package it.unipi.giar.Data;

import org.bson.Document;

public class Developer {
	private long id;
	private String name;
	private String slug;

	public Developer(Document document) {
		this.id =  (document.get("id") == null) ? 0 : document.getInteger("id");
		this.name = (document.get("name") == null) ? "" : document.getString("name");
		this.slug = (document.get("slug") == null) ? "" : document.getString("slug");
	}

	public Developer(long id, String name, String slug) {
		this.id = id;
		this.name = name;
		this.slug = slug;
	}
	
	public Developer(String name) {
		this.name = name;
	}

	public void setName(String name) {
		this.name = name;
	}

	public void setSlug(String slug) {
		this.slug = slug;
	}

	public long getId() {
		return this.id;
	}

	public String getName() {
		return this.name;
	}

	public String getSlug() {
		return this.slug;
	}

}
