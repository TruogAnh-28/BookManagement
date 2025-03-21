export interface BookInput {
  title: string;
  author: string;
  year: number;
  genre: string;
  description: string;
}

export interface Book extends BookInput {
  id: number;
}